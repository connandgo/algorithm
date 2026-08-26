"""Daily check-in bot.

Checks whether each user pushed a commit touching their folder in the last
24 hours (KST) and posts the result to Slack via an incoming webhook.
Runs as a scheduled GitHub Action; no third-party dependencies required.
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, time, timedelta, timezone

KST = timezone(timedelta(hours=9))


def get_commit_count(repo: str, user: str, since_iso: str, until_iso: str, token: str) -> int:
    url = (
        f"https://api.github.com/repos/{repo}/commits"
        f"?path={urllib.parse.quote(user)}&since={since_iso}&until={until_iso}&per_page=10"
    )
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "daily-checkin-bot",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return len(json.load(resp))


def post_slack(webhook_url: str, text: str) -> None:
    data = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url, data=data, headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)


def main() -> None:
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    users = [u.strip() for u in os.environ.get("USERS", "connandgo,dokwon33").split(",")]

    now_kst = datetime.now(KST)
    today_start = datetime.combine(now_kst.date(), time.min, tzinfo=KST)
    yesterday_start = today_start - timedelta(days=1)

    since_iso = yesterday_start.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    until_iso = today_start.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    results = {}
    for user in users:
        try:
            count = get_commit_count(repo, user, since_iso, until_iso, token)
        except urllib.error.HTTPError as e:
            print(f"GitHub API error for {user}: {e}", file=sys.stderr)
            count = 0
        results[user] = count > 0

    lines = [f"🌅 어제({yesterday_start.strftime('%Y-%m-%d')}) 문제 풀이 체크인"]
    for user, solved in results.items():
        mark = "✅" if solved else "❌"
        status = "풀었음" if solved else "아직 안 풀었음"
        lines.append(f"{mark} {user}: {status}")

    if all(results.values()):
        lines.append("\n둘 다 완료! 좋은 습관 유지 해나가는 중 👏")
    else:
        lines.append("\n오늘 몫도 화이팅 💪")

    post_slack(webhook_url, "\n".join(lines))


if __name__ == "__main__":
    main()
