#!/bin/zsh

set -u

readonly GH_BIN="/opt/homebrew/bin/gh"
readonly REPOSITORY="connandgo/algorithm"
readonly WORKFLOW="daily-checkin.yml"

for attempt in 1 2 3; do
  echo "[$(/bin/date '+%Y-%m-%d %H:%M:%S %Z')] Trigger attempt ${attempt}"

  if "$GH_BIN" workflow run "$WORKFLOW" --repo "$REPOSITORY" --ref main; then
    echo "GitHub Actions workflow dispatched successfully."
    exit 0
  fi

  if (( attempt < 3 )); then
    /bin/sleep 60
  fi
done

echo "Failed to dispatch GitHub Actions workflow after 3 attempts." >&2
exit 1
