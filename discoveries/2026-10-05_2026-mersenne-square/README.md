# 2026 → the sporadic square in 2ⁿ − 2n − 1

> **Best question:** For which n is 2ⁿ − 2n − 1 a perfect square? Equivalently: what is the largest number of the form 2ⁿ − 2n that is one more than a square?  · **Verification:** VERIFIED≤2·10⁶ (even n PROVEN)  · **Novelty:** NO-PRIOR-FOUND  · **Score:** 14/20

**Date:** 2026-10-05 · **Answer source:** pool (top seed)

## The answer
2026 = 2 · 1013 = 2¹¹ − 2·11 = 45² + 1 = 1 + (1³ + 2³ + ⋯ + 9³).

## Best new question(s)
1. **When is 2ⁿ − 2n − 1 a square? (14/20).** The only solutions with 1 ≤ n ≤ 2,000,000 are n = 3 (value 1) and n = 11 (value 2025 = 45²). So 2026 = 2¹¹ − 22 is the largest 2ⁿ − 2n of the form m² + 1. This is a Ramanujan–Nagell-type equation, 2ⁿ = x² + 2n + 1, and n = 11 is its one sporadic solution. The sibling forms 2ⁿ − n − 1, 2ⁿ − 2n + 1 and 2ⁿ + 2n + 1 have only tiny solutions (n ≤ 4).
   2ⁿ − 2n − 1 is OEIS [A070313](https://oeis.org/A070313), which also counts the dollars lost by a Martingale bettor over n trials with exactly one win. So the question is also "after how many trials can a Martingale loss be a perfect square?"
   *Verification.* Exact check for n ≤ 3000. Above that, a modular sieve over all primes < 2000 removes every n ≤ 2·10⁶, and it is rigorous: n is removed only when the value is a non-residue. A sanity run confirms the sieve keeps n = 3 and n = 11.
   *Proof for even n = 2k.* Write d = 2ᵏ − m. Then (2ᵏ−m)(2ᵏ+m) = 4k+1 gives d(2ᵏ⁺¹−d) = 4k+1 ≥ 2ᵏ⁺¹−1, which forces k ≤ 2, and neither k = 1 nor k = 2 works. Mod 8, odd solutions need n ≡ 3 (mod 4). The general odd case is **open**.
   *Equivalent form.* Which Eulerian numbers ⟨n,1⟩ = 2ⁿ−n−1 are sums of two consecutive squares? The answers are 1 and 1013 = 22² + 23² = ⟨10,1⟩, which is half of 2026.
2. **Coincidence (13/20, PROVEN).** 2ⁿ − 2n − 1 = 1³ + 2³ + ⋯ + (n−2)³ holds exactly for n = 3 and n = 11. In both solutions above, the square root happens to be C(n−1, 2), a triangular number. *Proof:* write L(n) = 2ⁿ−2n−1 and R(n) = C(n−1,2)². Then L(n+1) > 2L(n), and R(n+1)/R(n) < 2 for n ≥ 17. Since L(17) > R(17), L > R for all n ≥ 17. The cases n ≤ 16 are checked directly. Weaker than #1 because the index shift n−2 is somewhat arbitrary.

## Known questions excluded
2026 = 2·1013 (semiprime); 23 + 2003 (Goldbach); "evil" binary weight; digit-concatenation primes (t5k curios); 2025 = sum of the first nine cubes; compositions of 12 with no part used > 8 times ([A243086](https://oeis.org/A243086)); 2027 is a safe prime and 2026 = φ(2027).

## Novelty search log
| Query | Source | Result |
|---|---|---|
| 1,7,21,51,113,239,493,1003,2025 | OEIS | [A070313](https://oeis.org/A070313); full entry fetched: no mention of square terms |
| 2,8,22,52,…,2026 | OEIS | none by terms; [A005803](https://oeis.org/A005803) fetched: no mention of m²+1 terms or runs |
| 2,2026 · 4,12,2026 · "3,11 2^n-2n-1 square" · "2^n-2n-1 square" | OEIS | nothing relevant |
| 1,1013 · Eulerian terms + "square" | OEIS | Eulerian triangles only (A008292, A000295) |
| 1013 2026 | OEIS | A243086 → C4 KNOWN |
| "2^n - 2n - 1" perfect square solutions | Web | nothing on this expression |
| "2^n=x^2+2n+1" / "2^n-2n-1=x^2" diophantine | Web | only Ramanujan–Nagell and (aⁿ−1)(bⁿ−1)=x² papers → RELATED in spirit |
| math stackexchange 2^n−2n−1 square n=11 2025 | Web | nothing |
| "2^n - 2n - 1" sum of cubes / binomial(n-1,2)^2 | Web | nothing |
| 2026 = 2^11 − 22 = 45²+1 properties | Web | [t5k curios 2026](https://t5k.org/curios/page.php/2026.html) fetched: no such property |
| 2026 sum of first nine cubes plus one | Web | only "2025 = Σk³" pages |
| Eulerian 1013 = 22²+23² | Web | [DLMF 26.14](https://dlmf.nist.gov/26.14) gives ⟨10,1⟩ = 1013; no square-sum statement |
| binary strings ≥ 3 runs 2^n−2n | Web | not found stated (C3: RELATED, one-line derivation) |

## Verdict: **HIT** (C1 at 14/20; C2 at 13/20, a weak hit)
No prior statement was found in the searches listed here. That does not show the question is undiscovered. Completeness for odd n beyond 2·10⁶ is unproven.

## Files
- [candidates.md](candidates.md): all 20 candidates
- [verify.py](verify.py): checks and sieve (< 1 s)
