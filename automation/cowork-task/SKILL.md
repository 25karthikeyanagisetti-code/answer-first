---
name: answer-first-daily-research
description: Daily deep research run for answer-first. Take one answer, hunt for questions nobody has asked yet that it answers, verify them, search hard for prior art, and commit every finding to git.
---

You are running the daily research session for the **answer-first** project.

Repo: `~/Documents/Claude/Projects/AI system/answer-first`
(if it isn't there, look for a folder named `answer-first` under
`~/Documents/Claude/Projects/` and use that).

## What to do

1. `cd` into the repo.
2. Read `README.md`, `docs/method.md` and **`docs/deep_run.md`**.
3. Run the full protocol in `docs/deep_run.md`, Phases 0–9, in order.
   It is the source of truth; if this file and deep_run.md disagree, follow deep_run.md.

## Non-negotiables

- **Go deep.** Plan for 90–120 minutes. Don't settle for the first plausible
  question. Generate at least 40 candidates, verify far past A, run at least
  8 novelty queries per survivor, and do the skeptic pass. If round 1 gives no
  hit that survives the skeptic with a score of 13 or more, run round 2.
- **The goal is something new.** Questions that are already stated somewhere
  (OEIS, Wikipedia, MathWorld, papers, Prime Curios) are not hits, however
  pretty they are.
- **Honesty.** Never claim "undiscovered". Use the labels from the README.
  Never mark something PROVEN without a complete written proof. Every claim
  must be reproducible by running `verify.py`.
- **Everything goes in git.** Record all candidates (including killed and
  FALSE ones), the full search log, the skeptic notes, the scripts, and the
  daily-log, leaderboard, pool and open-problem updates. Then
  `git add -A && git commit`. Do **not** push; a separate job does that.
- **Always commit,** even on a MISS or a broken run. Use
  `daily: <A> — PARTIAL: <reason>` if you couldn't finish, and always delete
  `.run_in_progress` before you commit.
- Do not modify anything outside the answer-first repo.
