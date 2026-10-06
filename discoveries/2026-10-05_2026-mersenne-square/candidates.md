# Candidates: 2026

Bounds: C1 exact for n ≤ 3000, rigorous modular sieve (all primes < 2000) for n ≤ 2·10⁶. Goldbach counts to 2·10⁴. Lattice-point radii R² < 1500. Grid-graph screen m ≤ 6, n ≤ 8 (exploration only, not in verify.py).

| # | Question | Framing | Verification | Novelty | Score | Note |
|---|---|---|---|---|---|---|
| C1 | For which n is 2ⁿ−2n−1 a square? / largest 2ⁿ−2n that is m²+1 | Characterization / extremal | VERIFIED≤2e6 (even n PROVEN) | NO-PRIOR-FOUND (A070313 silent) | 14 | **HIT.** n ∈ {3, 11}; Ramanujan–Nagell-type |
| C2 | 2ⁿ−2n−1 = 1³+⋯+(n−2)³ only for n = 3, 11 | Coincidence | PROVEN | NO-PRIOR-FOUND | 13 | **HIT (weak).** Index shift is arbitrary |
| C5 | Eulerian ⟨n,1⟩ that are sums of two consecutive squares | Cross-domain | VERIFIED≤2e6 (≡ C1) | NO-PRIOR-FOUND | (= C1) | Gives 1013 = 2026/2 |
| C7 | 2026 is the only 2ⁿ−2n = m²+1 apart from 2 | Uniqueness | (≡ C1) | — | (= C1) | Same statement |
| C3 | Binary strings of length 11 with ≥ 3 runs = 2026 | Counting | PROVEN (enumeration) | RELATED (A005803) | 7 | One-line derivation |
| C19 | Subsets of [11] that are neither a prefix nor a suffix = 2026 | Counting | PROVEN | RELATED (A005803) | 6 | Same count as C3 |
| C4 | Compositions of 12 with no part used > 8 times | Counting | PROVEN | KNOWN (A243086) | 5 | |
| C6 | Smallest Eulerian ⟨n,1⟩ that is a Sophie Germain prime | Extremal | FALSE | — | — | answer is 11 (n=4) |
| C8 | Largest even n with exactly 32 Goldbach partitions | Extremal | FALSE | — | — | 2504 |
| C10 | Smallest composite m²+1 not a sum of ≥2 consecutive primes | Extremal | FALSE | — | — | 50 |
| C12 | Circle x²+y² ≤ R² with exactly 2026 lattice points | Cross-domain | FALSE | — | — | no R² < 1500 |
| C14 | Grid-graph spanning trees / independent sets / matchings = 2026 | Counting | FALSE | — | — | none for m ≤ 6, n ≤ 8 |
| C15 | Smallest m with (m²+1)/2, m²+2, m²+4 all prime | Extremal | FALSE (also gerrymandered) | — | — | m = 3 |
| C16 | Smallest m²+1 with σ = 2·square | Extremal | FALSE | — | — | 10 |
| C17 | Smallest prime p with (2ᵖ−2p)/2 prime | Extremal | FALSE | — | — | p = 5 |
| C18 | Smallest k with (1³+⋯+k³)+1 twice a prime | Extremal | FALSE | — | — | k = 2 |
| C9 | Pisano period π(n) = n+2 | Characterization | killed | — | — | 2026 is one of 96 below 6000 |
| C11 | 2026 = φ(2027), 2027 a safe prime with primitive root 2 | Uniqueness | killed | — | — | not distinguished |
| C13 | Binary reversal of 2026 is 703 = T₃₇ | Coincidence | killed | — | — | digit trivia |
| C20 | Roman numeral / calendar facts (2026 calendar = 2015) | Cross-domain | killed | — | — | not distinguished |

Controls (verify.py, n ≤ 3000): squares occur in 2ⁿ−n−1 at n = 1, 2, 3; in 2ⁿ−2n+1 at n = 1, 2, 4; in 2ⁿ+2n+1 at n = 2, 4; in 2ⁿ−2n at n = 1, 2. Only 2ⁿ−2n−1 has a large sporadic solution.
