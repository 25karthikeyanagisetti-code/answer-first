# Method: answer → undiscovered question

## 0. Definitions

- **Answer (A):** the given object, for example `1729`, `e^π`, `the Petersen graph`,
  `1, 2, 5, 14, 42`, or "water is densest at 4 °C".
- **Question (Q):** a statement-of-problem that **does not mention A** and
  whose unique (or distinguished) solution is A.
- **Hit:** a Q that is `VERIFIED≤N` or better, `NO-PRIOR-FOUND`, and scores ≥ 12/20.

## 1. Generate (≥15 candidates)

Cover at least 4 of these framings:

| Framing | Template |
|---|---|
| Extremal | "What is the smallest/largest X such that P?" |
| Uniqueness | "Which is the only X with property P?" |
| Characterization | "Find all X such that P." (A is the full solution set) |
| Coincidence | "When do two different constructions agree?" (A is where they meet) |
| Cross-domain | Recast A from another field (geometry ↔ number theory ↔ combinatorics ↔ physics) |
| Inverse | A is the output; ask for the process or input family that yields it |
| Counting | "How many X satisfy P?" = A |

Prefer properties that someone could care about *without* knowing A.

## 2. Kill list (reject immediately)

- Tautological: "the number equal to 1729", or P is defined as "being A".
- Gerrymandered: three or more arbitrary unrelated conditions glued together just to single out A.
- Base-10 digit trivia (unless the question is explicitly about bases).
- A is only one of many equally good solutions, with nothing that distinguishes it.

## 3. Verify

Write `verify.py` in the discovery folder. It must be runnable with
`.venv/bin/python verify.py` from the repo root and print PASS or FAIL for each candidate it checks.
Use exhaustive search with a stated bound, or a symbolic check (sympy). Write a
proof by hand only when it is short and fully stated. Any candidate that FAILS
is labelled `FALSE` and is not promoted.

## 4. Novelty search

For each verified survivor, search at minimum:
1. OEIS (`.venv/bin/python src/oeis.py "<terms or keyword>"`) whenever integers or sequences are involved.
2. Web search: the natural-language question, plus "A" together with the key property terms.
3. arXiv / MathWorld / Wikipedia for the property name.

Record **every query you ran** and its outcome in the write-up. Label the result
`KNOWN` (with link), `RELATED` (with links), or `NO-PRIOR-FOUND`.

## 5. Score (0–20)

| Axis | 0 | 5 |
|---|---|---|
| Naturalness | contrived | someone would ask this independently |
| Non-triviality | one-liner | needs real search or insight |
| Verification | conjectured | proven |
| Novelty | known | nothing related found |

## 6. Learning loop

At the end of each run, write down which framings produced hits. Add any
promising follow-ups (new answers suggested by today's work) to
`answers/pool.md` under `## Generated`.
