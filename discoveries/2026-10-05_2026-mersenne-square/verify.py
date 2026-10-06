"""Verify candidate questions whose answer is 2026.

Run from the repo root:
    .venv/bin/python discoveries/2026-10-05_2026-mersenne-square/verify.py
"""
import math
import time
import numpy as np
from sympy import isprime, primerange, factorint

T0 = time.time()
A = 2026


def report(tag, ok, msg):
    print(f"{tag}: {'PASS' if ok else 'FAIL'}  {msg}")


def is_sq(x):
    return x >= 0 and math.isqrt(x) ** 2 == x


# ---------------------------------------------------------------- C1
# All n >= 1 with 2^n - 2n - 1 a perfect square.
# (a) exact check n <= 3000; (b) rigorous modular sieve n <= NMAX:
#     n is discarded only if 2^n - 2n - 1 is a non-residue mod some prime q.
NMAX = 2_000_000
exact = [n for n in range(1, 3001) if is_sq(2 ** n - 2 * n - 1)]
alive = np.ones(NMAX + 1, bool)
alive[:3001] = False                     # already handled exactly
sanity = np.ones(NMAX + 1, bool)          # same sieve without the exclusion: 3 and 11 must survive
ns = np.arange(NMAX + 1, dtype=np.int64)
for q in primerange(3, 2000):
    qr = np.zeros(q, bool)
    qr[(np.arange(q) ** 2) % q] = True
    order = 1
    while pow(2, order, q) != 1:
        order += 1
    p2 = np.array([pow(2, i, q) for i in range(order)], dtype=np.int64)
    val = (p2[ns % order] - 2 * ns - 1) % q
    alive &= qr[val]
    sanity &= qr[val]
survivors = np.nonzero(alive)[0].tolist()
assert sanity[3] and sanity[11], "sieve wrongly discards a true solution"
print(f"C1-sieve: {int(sanity.sum())} values of n <= {NMAX:,} survive 300 prime moduli: {np.nonzero(sanity)[0].tolist()}")
survivors_exact = [n for n in survivors if is_sq(2 ** int(n) - 2 * int(n) - 1)]
sols = exact + survivors_exact
report("C1", sols == [3, 11],
       f"n with 2^n-2n-1 square, n<= {NMAX:,}: {sols} (sieve survivors beyond 3000: {survivors}); "
       f"values 2^n-2n = {[2**n-2*n for n in sols]}")

# C1 even case: n = 2k  =>  (2^k - m)(2^k + m) = 4k+1, d = 2^k - m >= 1 gives
# d(2^{k+1}-d) >= 2^{k+1}-1, so 2^k <= 2k+1, so k <= 2. Check k = 1, 2.
even_small = [2 * k for k in (1, 2) if is_sq(2 ** (2 * k) - 4 * k - 1)]
report("C1-even-proof", even_small == [] and all(2 ** k > 2 * k + 1 for k in range(3, 200)),
       "no even n >= 2 works (finite residue of the factoring argument checked)")
# C1 mod 8: for n >= 3 a solution needs n ≡ 3 (mod 4).
report("C1-mod8", all((n % 4 == 3) for n in sols), "both solutions are ≡ 3 mod 4, as forced mod 8")

# ---------------------------------------------------------------- C2
# 2^n - 2n - 1 = 1^3 + ... + (n-2)^3 = C(n-1,2)^2.  Proof that n in {3, 11} only:
# L(n) = 2^n-2n-1 satisfies L(n+1) = 2L(n) + 2n - 1 > 2L(n); R(n) = C(n-1,2)^2 satisfies
# R(n+1)/R(n) = (n/(n-2))^2 <= (17/15)^2 < 2 for n >= 17. L(17) > R(17), so by induction
# L > R for all n >= 17; the cases n <= 16 are checked directly.
def cubes(n):
    return (math.comb(n - 1, 2)) ** 2
c2 = [n for n in range(2, 201) if 2 ** n - 2 * n - 1 == cubes(n)]
grow = all((2 ** n - 2 * n - 1) > cubes(n) and 2 * (2 ** n - 2 * n - 1) - 1 > cubes(n + 1)
           for n in range(17, 201))
report("C2", c2 == [3, 11] and grow,
       f"n with 2^n-2n-1 = sum of first n-2 cubes: {c2}; 2^11-22 = {2**11-22} = 1+sum_(k<=9) k^3 = {1+sum(k**3 for k in range(1,10))}")

# ---------------------------------------------------------------- C3 / C19
def runs(s):
    return 1 + sum(1 for i in range(len(s) - 1) if s[i] != s[i + 1])
cnt = sum(1 for x in range(2 ** 11) if runs(format(x, "011b")) >= 3)
report("C3", cnt == A, f"binary strings of length 11 with >= 3 runs: {cnt}")
segs = set()
for k in range(12):
    segs.add(frozenset(range(1, k + 1)))
    segs.add(frozenset(range(12 - k, 12)))
report("C19", 2 ** 11 - len(segs) == A, f"subsets of [11] that are neither a prefix nor a suffix: {2**11-len(segs)}")

# ---------------------------------------------------------------- C4
def comps_maxmult(n, cap):
    # compositions of n with every part used at most `cap` times
    from functools import lru_cache
    total = 0
    # enumerate multiplicity vectors via partitions, count arrangements
    def parts(n, maxp):
        if n == 0:
            yield {}
            return
        for p in range(min(n, maxp), 0, -1):
            for m in range(1, n // p + 1):
                for rest in parts(n - p * m, p - 1):
                    d = dict(rest); d[p] = m
                    yield d
    for d in parts(n, n):
        if max(d.values()) <= cap:
            k = sum(d.values())
            ways = math.factorial(k)
            for m in d.values():
                ways //= math.factorial(m)
            total += ways
    return total
c4 = comps_maxmult(12, 8)
report("C4", c4 == A, f"compositions of 12 with no part used > 8 times: {c4}")

# ---------------------------------------------------------------- C5 (≡ C1)
eul = lambda n: 2 ** n - n - 1
cs = set(2 * k * (k + 1) + 1 for k in range(0, 10 ** 5))
c5 = [n for n in range(1, 60) if eul(n) in cs]
report("C5", c5 == [2, 10] and eul(10) * 2 == A,
       f"n with Eulerian <n,1> a sum of two consecutive squares (n<60, also implied by C1 to n<{NMAX:,}): {c5}, values {[eul(n) for n in c5]}")

# ---------------------------------------------------------------- C6
sg = [n for n in range(2, 200) if isprime(eul(n)) and isprime(2 * eul(n) + 1)]
report("C6", sg and 2 * eul(sg[0]) == A, f"smallest n with <n,1> a Sophie Germain prime: n={sg[0]}, value {eul(sg[0])}")

# ---------------------------------------------------------------- C8
M = 20000
sieve = np.ones(M + 1, bool); sieve[:2] = False
for i in range(2, int(M ** .5) + 1):
    if sieve[i]: sieve[i * i::i] = False
P = np.nonzero(sieve)[0]
G = np.zeros(M + 1, np.int64)
for p in P:
    if p > M // 2: break
    q = P[(P >= p) & (P <= M - p)]
    G[p + q] += 1
same = [n for n in range(4, M + 1, 2) if G[n] == G[A]]
report("C8", max(same) == A, f"largest even n<=2e4 with {G[A]} Goldbach partitions: {max(same)}")

# ---------------------------------------------------------------- C10
def consec_prime_sum(n, primes):
    for i in range(len(primes)):
        s = primes[i]
        for j in range(i + 1, len(primes)):
            s += primes[j]
            if s == n: return True
            if s > n: break
    return False
pl = list(primerange(2, 5000))
c10 = next(m * m + 1 for m in range(1, 70) if not isprime(m * m + 1) and not consec_prime_sum(m * m + 1, pl))
report("C10", c10 == A, f"smallest composite m^2+1 not a sum of >=2 consecutive primes: {c10}")

# ---------------------------------------------------------------- C12
pts = [R2 for R2 in range(1, 1500)
       if sum(2 * math.isqrt(R2 - x * x) + 1 for x in range(-math.isqrt(R2), math.isqrt(R2) + 1)) == A]
report("C12", bool(pts), f"R^2 with exactly 2026 lattice points in x^2+y^2<=R^2: {pts}")

# ---------------------------------------------------------------- C15
c15 = next(m for m in range(1, 1000, 2) if isprime((m * m + 1) // 2) and isprime(m * m + 2) and isprime(m * m + 4))
report("C15", c15 * c15 + 1 == A, f"smallest odd m with (m^2+1)/2, m^2+2, m^2+4 all prime: m={c15}")

# ---------------------------------------------------------------- C16
def sigma(n):
    s = 1
    for p, e in factorint(n).items(): s *= (p ** (e + 1) - 1) // (p - 1)
    return s
c16 = next(m * m + 1 for m in range(1, 100) if sigma(m * m + 1) % 2 == 0 and is_sq(sigma(m * m + 1) // 2))
report("C16", c16 == A, f"smallest m^2+1 with sigma = 2*square: {c16}")

# ---------------------------------------------------------------- C17
c17 = next(p for p in primerange(3, 100) if isprime((2 ** p - 2 * p) // 2))
report("C17", 2 ** c17 - 2 * c17 == A, f"smallest prime p with (2^p-2p)/2 prime: p={c17}")

# ---------------------------------------------------------------- C18
c18 = next(k for k in range(1, 100) if (math.comb(k + 1, 2) ** 2 + 1) % 2 == 0 and isprime((math.comb(k + 1, 2) ** 2 + 1) // 2))
report("C18", math.comb(c18 + 1, 2) ** 2 + 1 == A, f"smallest k with (1^3+..+k^3)+1 twice a prime: k={c18}")

# ---------------------------------------------------------------- C21/C22 (siblings, controls)
sib = {}
for name, f in [("2^n-n-1", lambda n: 2 ** n - n - 1), ("2^n-2n+1", lambda n: 2 ** n - 2 * n + 1),
                ("2^n+2n+1", lambda n: 2 ** n + 2 * n + 1), ("2^n-2n", lambda n: 2 ** n - 2 * n),
                ("2^n-2n-1 (C1)", lambda n: 2 ** n - 2 * n - 1)]:
    sib[name] = [n for n in range(1, 3001) if is_sq(f(n))]
print("C21/C22 (controls, n<=3000):", sib)

print(f"runtime {time.time()-T0:.1f}s")
