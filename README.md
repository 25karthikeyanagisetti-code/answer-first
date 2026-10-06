# answer-first

**We give the AI an answer. It looks for a question nobody has asked yet.**

Science usually goes question → answer. This project runs the other way. Start
from a known *answer*: a number, a sequence, a constant, a shape, an empirical
fact. Then search for **new questions that this answer resolves**. These are
questions that are natural, non-trivial, checkable, and have no prior statement
we can find.

> Example of the *shape* of a hit (this one is already known):
> Answer `1729` → Question *"What is the smallest number expressible as a sum of
> two positive cubes in two different ways?"*
> The goal is to find questions like this that **haven't** been written down yet.

## How a daily run works

```
answers/inbox.md  ──┐   (answers YOU give; checked first)
answers/pool.md   ──┼─► pick ONE answer
                    │
                    ▼
        1. Generate ≥15 candidate questions across framings
           (extremal, uniqueness, characterization, cross-domain, inverse)
        2. Kill trivial / tautological ones
        3. VERIFY that the answer really answers each one (Python: verify.py)
        4. NOVELTY search the survivors (OEIS, web, arXiv)
        5. Score and keep the best 1–3
                    │
                    ▼
        discoveries/<date>_<slug>/README.md + verify.py + candidates.md
        docs/daily_log.md, git commit (+ push if a remote exists)
```

The full method and scoring rubric are in [docs/method.md](docs/method.md).

## Honesty rules

We can't prove that a question is *undiscovered*. We can only say we didn't find
it. So every question gets two labels:

| Verification | Meaning |
|---|---|
| `PROVEN` | a short proof is written out |
| `VERIFIED≤N` | checked by computation up to a bound N |
| `CONJECTURED` | supported by evidence only |
| `FALSE` | the answer does not actually answer it (kept as a record) |

| Novelty | Meaning |
|---|---|
| `KNOWN` | found stated elsewhere (with link) |
| `RELATED` | close variants exist (with links) |
| `NO-PRIOR-FOUND` | searches listed in the write-up returned nothing |

## Give it an answer

Add a line under `## Queue` in [answers/inbox.md](answers/inbox.md). The next
daily run takes it before anything in the seed pool.

## Layout

| Path | What |
|---|---|
| `answers/inbox.md` | answers you give (priority queue) |
| `answers/pool.md` | seed answers used when the inbox is empty |
| `discoveries/` | one folder per daily run |
| `docs/method.md` | the procedure + scoring rubric |
| `docs/daily_log.md` | one entry per run |
| `docs/leaderboard.md` | best `NO-PRIOR-FOUND` questions so far |
| `src/oeis.py` | OEIS lookup helper for novelty checks |
