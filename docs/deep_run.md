# Deep daily run protocol

This is the playbook the daily scheduled task follows. It sits on top of
[method.md](method.md): method.md defines *what* a hit is; this file defines
*how hard* to look each day. Edit this file to change the daily behaviour.

**Goal of every run:** find at least one question that is genuinely new, true,
and natural, and leave a complete written record in git of everything tried,
including every failure.

**Effort budget:** plan for 90–120 minutes of real work. Do not stop early because
the first hit looks good. A run that finishes in under 45 minutes has skipped
something, and the log must say what.

---

## Phase 0 — Start (≈2 min)

1. `touch .run_in_progress` (autopush waits while this file exists).
2. Create `.venv` if it's missing and install `requirements.txt`.
3. Read `docs/daily_log.md` (last 5 entries), `docs/leaderboard.md`,
   `docs/open_problems.md`. Note which framings have been working.

## Phase 1 — Pick the answer (≈3 min)

Priority order, take the first available item:
1. `answers/inbox.md` → `## Queue`
2. `answers/pool.md` → `## Generated` (follow-ups from earlier runs)
3. `answers/pool.md` → `## Seeds`

Prefer answers that can be checked mechanically (integers, finite sequences,
finite objects). If the top item can't be checked by computation (a real
constant, a physical value), take it only if you can name a concrete
verification route (high-precision numerics, PSLQ, symbolic identities).
Otherwise skip it and leave it in place.

## Phase 2 — Property mining (≈15 min)

Before generating any question, **compute** a fact sheet for A in
`discoveries/<date>_<slug>/facts.md` (script: `mine.py`). Aim for 40+ facts:
- factorizations, representations (sums of squares/cubes, x²+ny², Löschian, …)
- memberships: run the neighbourhood of A through OEIS (A, A±1, 2A, A², nearby terms)
- arithmetic functions: φ, σ, λ, μ, ω, Ω, order of 2 and 10 mod A, …
- combinatorial / geometric / graph / physical interpretations
- **near-misses**: forms that A *almost* satisfies (these are where new questions hide)

Questions must come from this fact sheet, not from memory alone.

## Phase 3 — Generate, round 1 (≈15 min)

- **≥ 40 candidates.** At least 5 framings from method.md §1, with ≥ 5 candidates each.
- ≥ 8 must be **cross-domain** (the framing with the most hits so far).
- ≥ 5 must be **mutations** of past hits: take a winning structure from the
  leaderboard and ask whether A plays the same role in an analogous setting.
- Apply the kill list from method.md §2 and record every killed candidate with
  the reason.

## Phase 4 — Verify hard (≈20 min)

- Every surviving candidate gets a check in `verify.py`, which prints PASS or FAIL.
- Search bounds must be **at least 10× beyond** the point A occurs, and the
  write-up must state the bound.
- For each PASS: **compute the whole family** (the sequence for k = 1, 2, 3, …,
  or the full solution set up to the bound). Families make OEIS checks sharper
  and often expose a better question than the original one.
- Attempt a proof for every PASS. Write it out if it is short and complete.
  Otherwise label it `VERIFIED≤N` and record where the proof attempt got stuck.

## Phase 5 — Deep novelty search (≈20 min)

For every verified survivor, **at least 8 queries**, covering all of these:
1. OEIS by terms (the family from Phase 4), and OEIS by keywords
2. Web search with the natural-language question
3. Web search with A plus the key property words
4. arXiv full-text search for the property name
5. MathOverflow / Math StackExchange
6. MathWorld, Wikipedia (the page for A, and the page for the property)
7. t5k Prime Curios, Numbers Aplenty, or another number-trivia site, where relevant
8. Google Scholar or Semantic Scholar for the equation / family

**Open and read** the most relevant pages instead of judging by snippets. Log
every query and what came back in the write-up's search table.

## Phase 6 — Skeptic pass (≈10 min) — mandatory

Switch roles. You are now a referee whose job is to **reject** each candidate
that is still `NO-PRIOR-FOUND`. For each one, write in `skeptic.md`:
- 3 *new* prior-art queries you hadn't run yet, and their results
- the strongest case that it is gerrymandered or arbitrary
- the strongest case that it is trivial (a one-line reason)
- verdict: `SURVIVES` or `DOWNGRADED` (with new label/score)

Only `SURVIVES` candidates can be HITs.

## Phase 7 — Round 2 (if needed, ≈20 min)

If no candidate survived the skeptic **with score ≥ 13**, run another round
on the same A:
- ≥ 20 new candidates, using the framings that round 1 used *least*
- mine the near-misses from Phase 2 specifically
- repeat Phases 4–6 for the new survivors

If there is **still** no hit, the run is a `MISS`. Write down why A resisted
(this is a finding too), then go to Phase 8.

## Phase 8 — Deepen an open problem (≈15 min, skip if over budget)

Take the top item in `docs/open_problems.md` and push it forward: extend a
bound, try a proof technique, find the full family, or settle it. Record any
progress under that item, with the date. A real result here gets its own
section in today's write-up.

## Phase 9 — Write everything to git (≈10 min)

In `discoveries/<date>_<slug>/`:
- `README.md`: same structure as earlier runs (best questions, proofs, known
  questions excluded, full novelty search table, verdict)
- `candidates.md`: **every** candidate from both rounds, including killed and FALSE ones
- `facts.md`, `skeptic.md`, `mine.py`, `verify.py`

Update:
- `docs/daily_log.md`: one entry per run (format below)
- `docs/leaderboard.md`: add HITs, keep it sorted by score
- `docs/open_problems.md`: add new open questions that today's work raised
- `answers/pool.md`: move the used answer to `## Used`, and add ≥ 2 follow-up answers under `## Generated`
- `answers/inbox.md`: move a consumed inbox item to `## Done`

Then:
```
rm -f .run_in_progress
git add -A
git commit -m "daily: <A> — <HIT|MISS>: <one-line best question or reason>"
```
Do not push. The autopush job does that.

### Daily log entry format
```
## YYYY-MM-DD — <A>
- Source: inbox | generated | seed
- Effort: ~<minutes> min, rounds: 1|2
- Candidates: <gen> generated → <checked> checked (<killed> killed) → <pass> PASS / <fail> FALSE → <npf> NO-PRIOR-FOUND → <surv> survived skeptic
- Best: "<question>" (<verification>, <novelty>, <score>/20)
- Verdict: HIT | MISS
- Framings that worked / failed:
- Open problem progress: <item> — <what moved>
- Folder: discoveries/<date>_<slug>/
```

## If something breaks

Never end a run without committing. If a tool fails, the network is down, or
the time runs out, write what got done, what broke, and what's unfinished to
the daily log. Commit as `daily: <A> — PARTIAL: <reason>`, and remove
`.run_in_progress`.
