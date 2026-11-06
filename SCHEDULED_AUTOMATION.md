# Daily deep research — setup guide

This replaces the Snap-Time Agent daily research. It runs as a **Claude Code
cloud scheduled task** on Anthropic's servers, so it keeps going when your
laptop is closed, off, or with you on a hike. Each run clones this repo fresh
and pushes its results straight to `main`.

```
07:07 daily (cloud)  → fresh clone of answer-first
                     → orchestrator + 5 agents, ~140 min (docs/deep_run.md)
                       miner → generator → verifier ∥ prior-art-hunter → skeptic
                       → consensus (3 blind scores) → round 2 if no hit → open problem
                     → commit + push to main
```

Nothing runs on your Mac. No launchd, and no autopush.

---

## Step 1 — Turn off Snap-Time Agent

1. Cowork sidebar → **Scheduled** → `snap-time-agent-daily-research` → toggle **off** or delete it.
2. Terminal:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.snap-time-agent.autopush.plist 2>/dev/null
   rm -f ~/Library/LaunchAgents/com.user.snap-time-agent.autopush.plist
   ```

## Step 2 — Get this commit onto GitHub

The cloud task works from GitHub, not from your laptop, so `.claude/agents/`
and the docs have to be pushed.

## Step 3 — Create a cloud environment (network + setup)

The default environment only allows package registries, which would block
OEIS, arXiv and MathOverflow. At claude.ai/code, create an environment named
`answer-first-research`:

- **Network access → Custom**, keep "include default list" checked, and add:
  ```
  oeis.org
  arxiv.org
  export.arxiv.org
  mathoverflow.net
  math.stackexchange.com
  api.stackexchange.com
  mathworld.wolfram.com
  en.wikipedia.org
  t5k.org
  www.numbersaplenty.com
  api.semanticscholar.org
  scholar.google.com
  dlmf.nist.gov
  ```
  (Or choose **Full** if the agents keep running into blocked sites.)
- **Setup script:**
  ```bash
  pip install sympy numpy
  ```

## Step 4 — Create the scheduled task

Go to **claude.ai/code/routines** → **New task** (or **New routine**):

- **Name:** `answer-first-daily-research`
- **Prompt:** paste the contents of `automation/cloud-task/PROMPT.md`
- **Trigger:** Schedule → Daily, **7:07 AM** (a few minutes past the hour starts on time)
- **Repository:** `25karthikeyanagisetti-code/answer-first`
- **Environment:** `answer-first-research`
- **Model / effort:** your strongest model, at high effort
- **Connectors:** remove all of them (Gmail and Calendar aren't needed)

Click **Create**, then **Run now** once and watch the session to confirm that
it launches the agents and pushes to main.

## Day to day

- **Give it an answer:** add a line under `## Queue` in `answers/inbox.md` (editing on GitHub from your phone works).
- **Results:** `docs/daily_log.md`, `docs/leaderboard.md`, and the newest `discoveries/` folder on GitHub.
- **Pause:** claude.ai/code/routines → the task → toggle off.
- **Tune depth or roles:** edit `docs/deep_run.md` or `.claude/agents/*.md`.

## Things to know

- **Usage:** runs use your Claude subscription's usage, the same as interactive
  sessions. 140 minutes with 5 agents every day is heavy and can hit limits,
  especially on Pro. Check claude.ai/settings/usage after the first few runs.
  If you hit limits, run every other day or trim round 2 in deep_run.md.
- **GitHub connection:** if it expires, runs are skipped until you reconnect
  (the task turns itself off after 72 hours).
- **Run status:** "Succeeded" in History only means the session ended cleanly.
  Read the daily log to see whether it actually found anything.
- Scheduled tasks are a research preview, so details may change.
