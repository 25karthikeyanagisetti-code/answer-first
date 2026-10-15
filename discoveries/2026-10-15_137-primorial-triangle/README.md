# 137 → smallest Pythagorean triangle whose area is divisible by every prime ≤ 11

> **Best question:** What is the smallest hypotenuse of a primitive Pythagorean triangle whose area is divisible by every prime up to 11 (i.e. by 11# = 2310)?  · **Verification:** PROVEN (finite exhaustion of all PPTs with c ≤ 137)  · **Novelty:** NO-PRIOR-FOUND (RELATED: OEIS A263573)  · **Score:** 14/20

**Date:** 2026-10-15 · **Answer source:** pool (top seed)

## The answer
137: a prime, the inverse fine-structure constant rounded down, and 11² + 4².

## Best new question(s)
1. **Primorial-area triangle (14/20).** The (88, 105, 137) triangle has area 4620 = 2·2310. Every PPT area is divisible by 6, so the condition is really 5·7·11 | area. Dropping 5 does not give 137: 77 | area already happens at (33, 56, 65). An exhaustive check of all PPTs with c ≤ 137 shows no smaller hypotenuse, so the result is proven. Across the family k ↦ p_k#, the smallest hypotenuses are **5, 13, 29, 137, 569, 1597, 10957, 51781** for k = 2..9 (exact, since the search covers every c < 1.156·10⁷). OEIS has no match.
   **Twist:** 11# is the first primorial where the smallest-hypotenuse triangle is *not* the smallest-area one. The triangle with area exactly 2310 is (21, 220, 221). For 3#, 5#, 7#, 13# and 17#, the two triangles coincide; for 7# it is (20, 21, 29) and for 17# it is (715, 1428, 1597), with area exactly 510510 and 1597 a Fibonacci prime.
2. *(Not a hit, 10/20)* The smallest E-irregular prime ≡ 1 (mod 8) is 137. It is checked directly against the E-irregular primes below 290, and it is RELATED to a paper on the mod-8 distribution of E-irregular primes.

## Known questions excluded
⌊1/α⌋ (fine-structure constant) and the Dirac Z > 137 limit; Stern prime (Goldbach's other conjecture); numerator of H₅ = 137/60 (expected number of cycles in S₅); 1/137 has period 8, and 10⁴+1 = 73·137; 33rd prime; Pythagorean prime 11²+4²; twin prime with 139; Chen prime; E-irregular prime.

## Novelty search log
| Query | Source | Result |
|---|---|---|
| 5,13,29,137,569,1597,10957 | OEIS | no results |
| 13,29,137,569,1597 | OEIS | no results |
| 6,30,210,4620,60060,510510 | OEIS | no results |
| 6,30,210,2310,60060,510510,29099070 | OEIS | no results |
| 19,31,43,47,61,67,71,79,101,137,139 | OEIS | [A120337](https://oeis.org/A120337) (E-irregular primes) |
| 1,3,11,25,137,49,363 | OEIS | [A001008](https://oeis.org/A001008) (H_n numerators) → C14 KNOWN |
| primitive Pythagorean triangle area divisible by 2310 smallest hypotenuse 137 | Web | nothing matching |
| Pythagorean triangle 88 105 137 area 4620 | Web | only triple lists / area lists ([A024365](https://oeis.org/A024365)) |
| PPT area divisible by primorial, smallest hypotenuse sequence | Web | nothing matching |
| PPT area equal to primorial 210 2310 30030 510510 | Web | [A263573](https://oeis.org/A263573): PPT areas that are products of primorials (4620 is listed). No hypotenuse question → RELATED |
| PPT area divisible by 5, 7 and 11 smallest | Web | only same-area triangle facts ([ProofWiki](https://www.proofwiki.org/wiki/Smallest_Triplet_of_Pythagorean_Triangles_with_Same_Area)) |
| A263573 page | WebFetch | no mention of hypotenuse, 137 or "smallest" |
| smallest E-irregular prime ≡ 1 mod 8 | Web | [AFM paper on the mod-8 distribution of E-irregular primes](https://afm.journal.fi/article/view/134253) → RELATED (abstract not readable) |
| harmonic numerator 137 first prime ≡ 1 mod 4 | Web | A001008 / [Wikipedia](https://en.wikipedia.org/wiki/Harmonic_number) only → RELATED |

## Verdict: **HIT** (C1, 14/20)
No prior statement of C1 or of its primorial sequence was found in the searches listed here. That does not show the question is undiscovered.

## Files
- [candidates.md](candidates.md): all candidates
- [verify.py](verify.py): exhaustive checks (~9 s)
