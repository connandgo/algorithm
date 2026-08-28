# algorithm
프로그래머스 코딩 테스트 준비를 위한 저장소입니다. (`level 1`, `level 2`, `level 3` 폴더는 과거 [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)로 자동 커밋되던 백준 풀이 기록입니다.)

## 프로그래머스 하루 1솔 체크인

각자 매일 프로그래머스 풀이를 본인 GitHub 계정으로 커밋합니다.
매일 08:00(KST)에 GitHub Actions가 전날 각 사용자가 작성한 커밋이 있는지 확인해 Slack으로 알려줍니다.

### 설정 (최초 1회)

1. Slack 워크스페이스에서 [Incoming Webhook](https://api.slack.com/messaging/webhooks)을 생성해 알림 받을 채널의 Webhook URL을 발급받습니다.
2. 이 저장소 `Settings > Secrets and variables > Actions`에서 `SLACK_WEBHOOK_URL` 이름으로 시크릿을 등록합니다.
3. 그 외 별도 설정은 필요 없습니다. `.github/workflows/daily-checkin.yml`이 매일 자동 실행됩니다.
4. 바로 테스트하려면 저장소의 `Actions` 탭 > `Daily Solve Check-in` > `Run workflow`로 수동 실행할 수 있습니다.

### macOS 정시 실행

GitHub 예약 실행의 지연이나 누락을 보완하기 위해 macOS `launchd`가 매일 08:00(KST)에
워크플로를 직접 호출합니다. GitHub 예약 실행과 겹쳐도 날짜별 캐시로 Slack 알림은 한 번만 전송됩니다.

- LaunchAgent: `launchd/com.connandgo.algorithm-daily-checkin.plist`
- 호출 스크립트: `scripts/trigger_daily_checkin.sh`
- 실행 로그: `~/Library/Logs/algorithm-daily-checkin.log`
