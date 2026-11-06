# Daily deep research — install guide

This replaces the Snap-Time Agent daily research.

## Architecture

```
07:00        Cowork scheduled task "answer-first-daily-research" wakes up
             → follows docs/deep_run.md (~90–120 min)
             → property mining, ≥40 candidates, verification, deep novelty search,
               skeptic pass, round 2 if no hit, open-problem push
             → writes everything to discoveries/<date>_<slug>/ and docs/
             → git commit (locally; the sandbox can't push)

09:30 / 11:30 / 14:00   launchd runs scripts/autopush.sh
             → waits if .run_in_progress exists (the run is still going)
             → git push origin main
             → log: ~/Library/Logs/answer-first-autopush.log
```

The Mac has to be awake at 07:00 for the research to run. launchd catches up
on missed push slots when the Mac wakes.

---

## Step 1 — Turn off Snap-Time Agent

1. Cowork sidebar → **Scheduled** → `snap-time-agent-daily-research` → toggle **off**
   (or delete it).
2. Terminal:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.snap-time-agent.autopush.plist 2>/dev/null
   rm -f ~/Library/LaunchAgents/com.user.snap-time-agent.autopush.plist
   launchctl list | grep snap-time-agent   # should print nothing
   ```

## Step 2 — Put the repo where the task expects it

The task and autopush expect: `~/Documents/Claude/Projects/AI system/answer-first`
```bash
ls ~/Documents/Claude/Projects/"AI system"/answer-first/docs/deep_run.md
```
If the repo is somewhere else, move it there, or change the path in
`automation/cowork-task/SKILL.md`, in `scripts/autopush.sh` (`REPO=`), and in
`scripts/com.user.answer-first.autopush.plist`.

## Step 3 — Create the Cowork scheduled task

In Cowork, with the answer-first folder connected, ask Claude:

> Create a scheduled task named `answer-first-daily-research` that runs daily at
> 7:00 AM (`0 7 * * *`). Use the contents of `automation/cowork-task/SKILL.md`
> in this repo as its instructions. Give it read/write access to the
> answer-first folder.

Then click **Run now** once to test it. Make sure it can write files; the
Oct 15 run hit a sandbox write block.

## Step 4 — Install auto-push

```bash
R=~/Documents/Claude/Projects/"AI system"/answer-first
chmod +x "$R/scripts/autopush.sh"
git config --global credential.helper osxkeychain
cp "$R/scripts/com.user.answer-first.autopush.plist" ~/Library/LaunchAgents/
launchctl unload ~/Library/LaunchAgents/com.user.answer-first.autopush.plist 2>/dev/null
launchctl load   ~/Library/LaunchAgents/com.user.answer-first.autopush.plist
launchctl list | grep answer-first
```

## Step 5 — Test the push once

```bash
"$R/scripts/autopush.sh"; echo "exit: $?"
tail -20 ~/Library/Logs/answer-first-autopush.log
```
`OK: pushed` or `nothing new to push` means it works. `push failed` usually
means an expired GitHub token: do one manual `git push` and enter your PAT.

---

## Day to day

- **Give it an answer:** add a line under `## Queue` in `answers/inbox.md`
  (you can do this on GitHub; autopush rebases before it pushes).
- **Change how deep it goes:** edit `docs/deep_run.md`.
- **See results:** `docs/daily_log.md`, `docs/leaderboard.md`, and the newest folder in `discoveries/`.
- **Pause:** Cowork → Scheduled → toggle off.

## Troubleshooting

| Symptom | Check |
|---|---|
| No new folder today | Cowork → Scheduled → run history; was the Mac awake at 7:00? |
| Committed but not on GitHub | `tail ~/Library/Logs/answer-first-autopush.log` |
| Log says "research still running" all day | Remove the stale `.run_in_progress` (autopush does this by itself after 4 h) |
| `PARTIAL` commits | Read that day's daily_log entry; it says what broke |
