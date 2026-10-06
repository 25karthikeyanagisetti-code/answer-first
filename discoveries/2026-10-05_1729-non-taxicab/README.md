# 1729 → smallest Carmichael number that is an Eisenstein norm

> **Best question:** What is the smallest Carmichael number of the form x² + xy + y² (a norm of an Eisenstein integer)?  · **Verification:** PROVEN (+ VERIFIED≤2·10⁷)  · **Novelty:** NO-PRIOR-FOUND  · **Score:** 15/20

**Date:** 2026-10-05 · **Answer source:** inbox (hint: "a question about 1729 that isn't the taxicab one")

## The answer
1729 = 7 · 13 · 19, a Carmichael number.

## Best new question(s)
1. **Smallest Carmichael Eisenstein norm (15/20).** It is the Z[ω] twin of the Gaussian case: 1105 = 5·13·17 is the smallest Carmichael number that is a sum of two squares (verify.py checks this as a control).
   *Proof.* A squarefree n is a norm x²+xy+y² iff each prime factor is 3 or ≡ 1 (mod 3). If 3 | n and n is Carmichael, then every other prime p | n has 3 | p−1 | n−1, which contradicts 3 | n. So all prime factors are ≡ 1 (mod 6), and there are at least 3 of them. The smallest such product is 7·13·19 = 1729, which satisfies Korselt's criterion. ∎ The same holds for "all prime factors ≡ 1 mod 3" (C14).
   An exhaustive check over the 141 Carmichael numbers ≤ 2·10⁷ agrees. The sequence starts 1729, 2821, 8911, 15841, 29341, 46657, … and is not in OEIS.
2. **Smallest Carmichael number with λ(n)² < n (12/20, weak).** λ(1729) = 36 < √1729 ≈ 41.6, while λ(561) = 80 and λ(1105) = 48 are both larger than √n. Proven by checking these three cases. Related: OEIS A277389 (λ³ | (n−1)²) also starts with 1729.
3. *(Not a hit, 11/20)* The numbers that are both centered-cube and 12-gonal: {1, 1729, 6034609, 3391605945, 5227631785} for k < 10⁶. These are integer points on a genus-1 curve, so the list should be finite (Siegel). Completeness is CONJECTURED.

## Known questions excluded
Taxicab Ta(2); Fermat near-miss 9³+10³ = 12³+1; third Carmichael number; smallest Chernick (6k+1)(12k+1)(18k+1) number; smallest absolute Euler pseudoprime; Zeisel number; centered-cube number; 12-gonal number; Harshad trivia (1+7+2+9 = 19, 19·91 = 1729).

## Novelty search log
| Query | Source | Result |
|---|---|---|
| 1,49,637,1729,8281,12103 | OEIS | none; but C1 is on Wikipedia → KNOWN |
| 1,7,49,91,637,1729,… | OEIS | A230655 (hex-lattice records) → C2 KNOWN |
| 1729,2465,29341,… | OEIS | A300949 → C4 KNOWN |
| 1729,46657,2433601,… | OEIS | A265328 → C9 KNOWN |
| 1729,46657,2628073 | OEIS | A265628 (Carmichael k³+1) |
| 1729,63973,75361,… | OEIS | A272798, A290805 → C6 KNOWN |
| 1729,63973,656601,825265,997633 (λ square) | OEIS | none |
| 1729,2821,8911,15841,29341,46657,52633 | OEIS | **none** |
| 1729,41041,63973,75361,101101 (λ²<n) | OEIS | none |
| 1,1729,6034609 / 1729,75361,340561 / 12,36,138,… | OEIS | none |
| "carmichael x^2+xy+y^2", "carmichael lambda square" | OEIS text | nothing relevant (A173694 is λ square for all n) |
| smallest a²+ab+b² in four ways 1729 | Web | [Wikipedia 1729](https://en.wikipedia.org/wiki/1729_(number)) states it → C1 KNOWN |
| Carmichael all prime factors ≡1 mod 6 smallest 1729 | Web | only Chernick-form statements ([t5k curios](https://t5k.org/curios/cpage/44550.html)) |
| smallest Carmichael number that is a norm of an Eisenstein integer | Web | nothing found |
| Carmichael numbers of the form x²+xy+y² / Loeschian Carmichael | Web | only general Löschian pages ([Wikipedia](https://en.wikipedia.org/wiki/L%C3%B6schian_number)) |
| "Carmichael" "prime factors" "6k+1" 2821 8911 15841 | Web | general Carmichael lists only |
| Carmichael lambda perfect square; λ(n)²<n | Web | [A276980](https://oeis.org/A276980), [A277366](https://oeis.org/A277366), [A277389](https://oeis.org/A277389) → RELATED |
| centered cube ∩ dodecagonal, 6034609 | Web | Wikipedia lists both properties of 1729; no intersection list found |
| Wikipedia / number.subwiki pages for 1729 | WebFetch | neither page mentions Eisenstein norms, λ², or primes ≡1 mod 3 |

## Verdict: **HIT** (two questions: C3 at 15/20, C13 at 12/20)
No prior statement of C3 was found in the searches listed here. That does not show it is undiscovered.

## Files
- [candidates.md](candidates.md): all 22 candidates
- [verify.py](verify.py): exhaustive checks (~11 s)
