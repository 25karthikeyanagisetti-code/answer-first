#!/usr/bin/env bash
# Pushes commits made by the daily Cowork research task for answer-first.
# Runs from launchd several times each morning. It is a no-op when there is
# nothing new, and it waits while a research run is still in progress.
#
# Log: ~/Library/Logs/answer-first-autopush.log

set -u
LOG="$HOME/Library/Logs/answer-first-autopush.log"
REPO="${ANSWER_FIRST_REPO:-$HOME/Documents/Claude/Projects/AI system/answer-first}"
GIT_AUTHOR_EMAIL="25karthikeyanagisetti@gmail.com"
GIT_AUTHOR_NAME="Karthikeya Nagisetti"
STALE_LOCK_MIN=240   # a .run_in_progress older than this is treated as a crashed run

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*" >> "$LOG"; }
log "===== autopush start ====="

[ -d "$REPO/.git" ] || { log "ERROR: repo not found at $REPO"; exit 1; }
cd "$REPO" || exit 1

git config user.email "$GIT_AUTHOR_EMAIL"
git config user.name  "$GIT_AUTHOR_NAME"

# Wait if today's research is still running.
if [ -f .run_in_progress ]; then
  AGE_MIN=$(( ( $(date +%s) - $(stat -f %m .run_in_progress 2>/dev/null || stat -c %Y .run_in_progress) ) / 60 ))
  if [ "$AGE_MIN" -lt "$STALE_LOCK_MIN" ]; then
    log "research still running (${AGE_MIN} min); skipping, will retry next slot"
    exit 0
  fi
  log "WARNING: stale .run_in_progress (${AGE_MIN} min), run probably crashed; removing"
  rm -f .run_in_progress
fi

# Clear lock files the Cowork sandbox can leave behind.
rm -f .git/index.lock .git/HEAD.lock
git checkout main >> "$LOG" 2>&1

# Commit anything Claude forgot to commit, so nothing is lost.
if [ -n "$(git status --porcelain)" ]; then
  log "WARNING: uncommitted changes found; safety commit"
  git add -A
  git commit -m "autopush: safety commit of uncommitted research files" >> "$LOG" 2>&1
fi

# Nothing to push? Done. (No fake heartbeat commits: history = real runs only.)
git fetch origin main >> "$LOG" 2>&1
AHEAD=$(git rev-list --count origin/main..main 2>/dev/null || echo 1)
if [ "$AHEAD" -eq 0 ]; then
  log "nothing new to push"
  exit 0
fi

# Rebase in case you pushed from elsewhere (e.g. added to the inbox on GitHub).
git pull --rebase origin main >> "$LOG" 2>&1 || { log "ERROR: rebase failed, resolve by hand"; git rebase --abort >> "$LOG" 2>&1; exit 1; }

git push origin main >> "$LOG" 2>&1
RC=$?
[ $RC -eq 0 ] && log "OK: pushed $AHEAD commit(s)" || log "ERROR: push failed rc=$RC (check GitHub credential)"
log "===== autopush end ====="
exit $RC
