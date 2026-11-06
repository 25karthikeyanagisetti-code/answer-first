# Deep daily run protocol

This is the playbook the daily cloud scheduled task follows. It sits on top of
[method.md](method.md): method.md defines *what* a hit is; this file defines
*how hard* to look each day and *who does what*. Edit this file to change the
daily behaviour.

**Goal of every run:** find at least one question that is genuinely new, true,
and natural, assessed independently by several agents, and leave a complete
written record in git of everything tried, including every failure.

**Effort budget: 140 minutes.** Use the whole budget. If the run ends under
100 minutes, the daily log must say which phases were cut short and why.

## The team

The main session is the **orchestrator**. It never generates, verifies, or
judges novelty itself. It launches 5 subagents (defined in `.claude/agents/`),
passes them the answer and the folder path, and merges what they return.

| Agent | Job | Writes |
|---|---|---|
| `miner` | compute 40+ facts and near-misses about A | `mine.py`, `facts.md` |
| `generator` | 40+ candidate questions (20+ in round 2), kill list | `candidates.md` |
| `verifier` | independent computation, families, proofs, score | `verify.py`, `verification.md`, `scores.md` |
| `prior-art-hunter` | ≥ 8 searches per candidate, novelty label, score | `novelty.md`, `scores.md` |
| `skeptic` | independent re-check, new searches, gerrymander/triviality tests, verdict, score | `skeptic_check.py`, `skeptic.md`, `scores.md` |

**Independence rules:** the verifier, prior-art-hunter and skeptic each score
**blind** to the other two columns in `scores.md`. The skeptic writes its own
check before it reads verify.py.

---

## Phase 0 — Start (≈3 min) · orchestrator
1. `git pull --rebase origin main` so you have any inbox items added on GitHub.
2. `python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt`
3. Read the last 5 entries of `docs/daily_log.md`, plus `docs/leaderboard.md` and `docs/open_problems.md`.
4. Note the start time. Budget the phases below to finish by **start + 140 min**.

## Phase 1 — Pick the answer (≈2 min) · orchestrator
Take the first available item, in this order:
1. `answers/inbox.md` → `## Queue`
2. `answers/pool.md` → `## Generated`
3. `answers/pool.md` → `## Seeds`

Prefer answers that can be checked mechanically. Skip an answer, and leave it
in place, if there's no concrete verification route. Create
`discoveries/<YYYY-MM-DD>_<slug>/`.

## Phase 2 — Property mining (≈15 min) · `miner`

## Phase 3 — Generate, round 1 (≈15 min) · `generator`

## Phase 4+5 — Verify ∥ prior-art search (≈30 min) · `verifier` and `prior-art-hunter` **in parallel**
Launch both on all surviving candidates at the same time. When the verifier
returns families, pass them to the prior-art-hunter so it can check them in
OEIS by terms (re-launch it for that follow-up if it has already finished).
FALSE candidates go no further.

## Phase 6 — Skeptic pass (≈20 min) · `skeptic` — mandatory
Run on every candidate that is PASS and NO-PRIOR-FOUND.

## Phase 7 — Consensus and round 2 (≈30 min) · orchestrator
For each candidate in `scores.md`, compute the **median** of the three
independent scores (verifier, prior_art, skeptic) and the **spread** (max − min).

A **consensus HIT** needs all of these:
- verification is `VERIFIED≤N` or `PROVEN` (and the skeptic's re-check agrees)
- novelty is `NO-PRIOR-FOUND` from the prior-art-hunter, and the skeptic found no prior art
- the skeptic's verdict is `SURVIVES`
- median ≥ 13 **and** no single score below 10

If the spread is ≥ 6, write one paragraph in the README explaining the
disagreement. Disagreement is information.

If there's no consensus HIT, run **round 2**: `generator` (round 2), then
`verifier` ∥ `prior-art-hunter`, then `skeptic`, then consensus again. If there's
still no hit, the run is a `MISS`. Write down why A resisted, because that is a finding too.

## Phase 8 — Deepen an open problem (≈15 min, less if round 2 ran) · `verifier`
Send the top item from `docs/open_problems.md` to the verifier: extend a bound,
try a proof, compute the family, or settle it. Record progress under that item,
with the date.

## Phase 9 — Write to git and push (≈10 min) · orchestrator

In `discoveries/<date>_<slug>/` you should now have: `README.md` (written by
the orchestrator, in the same structure as earlier runs, plus a **Team
assessment** table of the three scores, median and spread for every candidate
that reached scoring), `facts.md`, `mine.py`, `candidates.md`, `verify.py`,
`verification.md`, `novelty.md`, `skeptic.md`, `skeptic_check.py` and `scores.md`.

Update:
- `docs/daily_log.md`: one entry (format below)
- `docs/leaderboard.md`: consensus HITs only, sorted by median
- `docs/open_problems.md`: add new open threads
- `answers/pool.md`: used answer → `## Used`; add ≥ 2 follow-ups under `## Generated`
- `answers/inbox.md`: consumed item → `## Done`

Then commit and **push straight to main**:
```
git add -A
git commit -m "daily: <A> — <HIT|MISS>: <one-line best question or reason>"
git pull --rebase origin main
git push origin HEAD:main
```
If the push to main is rejected, push to `claude/daily-<date>` instead and say
so in the daily log.

### Daily log entry format
```
## YYYY-MM-DD — <A>
- Source: inbox | generated | seed
- Effort: ~<minutes> min, rounds: 1|2
- Candidates: <gen> generated → <checked> checked (<killed> killed) → <pass> PASS / <fail> FALSE → <npf> NO-PRIOR-FOUND → <surv> survived skeptic → <hits> consensus HIT
- Best: "<question>" (<verification>, <novelty>, median <m>/20, scores v/p/s = <a>/<b>/<c>)
- Verdict: HIT | MISS
- Agent disagreements: <where the spread was ≥ 6, and why>
- Framings that worked / failed:
- Open problem progress: <item> — <what moved>
- Folder: discoveries/<date>_<slug>/
```

## If something breaks
Never end a run without committing and pushing. If an agent fails, the network
blocks a source, or time runs out, write down what got done, what broke, and
what's unfinished. Commit as `daily: <A> — PARTIAL: <reason>` and push.
