"""Verify candidate questions whose answer is 1729 (excluding the taxicab one).

Run from repo root:  .venv/bin/python discoveries/2026-10-05_1729-non-taxicab/verify.py
Bounds are printed with each result.
"""
import math
import time

import numpy as np
from sympy import divisors, factorint, isprime

T0 = time.time()
A = 1729
N_CARM = 20_000_000  # Carmichael numbers enumerated exhaustively below this bound


def report(tag, ok, msg):
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}  {msg}")


# ---------------------------------------------------------------- sieve + Carmichael list
spf = np.zeros(N_CARM + 1, dtype=np.int32)
for p in range(2, int(N_CARM ** 0.5) + 1):
    if spf[p] == 0:
        blk = spf[p * p :: p]
        blk[blk == 0] = p
is_prime = spf == 0
is_prime[:2] = False


def factor(n):
    f = {}
    while n > 1:
        p = int(spf[n]) or n
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def korselt(n, f):
    return len(f) >= 2 and all(e == 1 for e in f.values()) and all((n - 1) % (p - 1) == 0 for p in f)


carm = []
for n in range(3, N_CARM + 1, 2):
    if is_prime[n] or pow(2, n - 1, n) != 1:
        continue  # every odd Carmichael number is a base-2 Fermat pseudoprime
    f = factor(n)
    if korselt(n, f):
        carm.append((n, sorted(f)))
print(f"# {len(carm)} Carmichael numbers <= {N_CARM:,} (sanity: count ≤1e7 printed next; known value 105); first: {[c[0] for c in carm[:4]]}")
print(f"# Carmichael count <= 1e7: {sum(1 for c in carm if c[0] <= 10**7)}")


def lam(ps):
    return math.lcm(*[p - 1 for p in ps])


def phi(ps):
    return math.prod(p - 1 for p in ps)


def is_square(x):
    r = math.isqrt(x)
    return r * r == x


def is_perfect_power(x):
    for k in range(2, x.bit_length() + 1):
        r = round(x ** (1 / k))
        for c in (r - 1, r, r + 1):
            if c > 1 and c ** k == x:
                return True
    return False


def first(pred):
    for n, ps in carm:
        if pred(n, ps):
            return n
    return None


def allc(pred):
    return [n for n, ps in carm if pred(n, ps)]


# ---------------------------------------------------------------- Carmichael extremal candidates
lo3 = lambda n, ps: all(p == 3 or p % 3 == 1 for p in ps)  # norm from Z[omega] (squarefree n)
r = first(lo3)
report("C3", r == A, f"smallest Carmichael that is a norm x^2+xy+y^2 (all p=3 or p≡1 mod 3): {r}  (N={N_CARM:,})")
r = first(lambda n, ps: all(p % 3 == 1 for p in ps))
report("C14", r == A, f"smallest Carmichael with all prime factors ≡1 mod 3: {r}")
r4 = first(lambda n, ps: all(p % 4 == 1 for p in ps))
print(f"     (control: smallest Carmichael with all p≡1 mod 4, i.e. sum of two squares: {r4})")


def in_ap(ps):
    d = ps[1] - ps[0]
    return all(ps[i + 1] - ps[i] == d for i in range(len(ps) - 1))


r = first(lambda n, ps: in_ap(ps))
apc = allc(lambda n, ps: in_ap(ps))
report("C4", r == A, f"smallest Carmichael whose prime factors form an AP: {r}; all ≤N: {apc}")

r = first(lambda n, ps: is_square(phi(ps)))
report("C6", r == A, f"smallest Carmichael with phi(n) a perfect square: {r}")
r = first(lambda n, ps: is_square(lam(ps)))
report("C7", r == A, f"smallest Carmichael with lambda(n) a perfect square: {r}")
eq = allc(lambda n, ps: phi(ps) == lam(ps) ** 2)
report("C8", eq == [A], f"Carmichael n ≤ N with phi(n) = lambda(n)^2: {eq}")
r = first(lambda n, ps: is_perfect_power(n - 1))
pp = allc(lambda n, ps: is_perfect_power(n - 1))
report("C9", r == A, f"smallest Carmichael with n-1 a perfect power: {r}; all ≤N: {pp}")
r = first(lambda n, ps: lam(ps) ** 2 < n)
report("C13", r == A, f"smallest Carmichael with lambda(n)^2 < n: {r}")
cubes = {k ** 3 for k in range(1, 300)}
r = first(lambda n, ps: any((n - c) in cubes for c in cubes if c < n))
report("C19", r == A, f"smallest Carmichael that is a sum of two positive cubes: {r}")

# ---------------------------------------------------------------- C5: 3-prime AP Carmichael characterisation
D = 3000
ap3 = []
for d in range(1, D + 1):
    for m in divisors(d * d):  # q-1 = p+d-1 must divide d^2
        p = m - d + 1
        if p < 2:
            continue
        q, rr = p + d, p + 2 * d
        if not (isprime(p) and isprime(q) and isprime(rr)):
            continue
        n = p * q * rr
        if all((n - 1) % (x - 1) == 0 for x in (p, q, rr)):
            ap3.append((n, p, d))
ap3.sort()
nonch = [(n, p, d) for n, p, d in ap3 if not (d % 6 == 0 and p == d + 1)]
report("C5", not nonch, f"all 3-prime AP Carmichael (d≤{D}) are Chernick (6k+1)(12k+1)(18k+1): "
       f"{len(ap3)} found, smallest={ap3[0][0]}, non-Chernick={nonch[:5]}")
report("C4b", ap3[0][0] == A, f"smallest 3-prime AP Carmichael over all p, d≤{D}: {ap3[0][0]}")

# ---------------------------------------------------------------- C10: Carmichael numbers b^3+1
B = 20000
cub = []
for b in range(2, B + 1):
    f = factorint(b + 1)
    for k, v in factorint(b * b - b + 1).items():
        f[k] = f.get(k, 0) + v
    n = b ** 3 + 1
    if korselt(n, f):
        cub.append(b)
report("C10", cub == [12], f"b≤{B:,} with b^3+1 Carmichael: {cub}")
B2 = 300000
sq = []
for b in range(2, B2 + 1):
    n = b * b + 1
    if n % 2 == 0 or isprime(n) or pow(2, n - 1, n) != 1:
        continue
    if korselt(n, factorint(n)):
        sq.append(b)
print(f"     (context: b≤{B2:,} with b^2+1 Carmichael: {sq[:10]})")

# ---------------------------------------------------------------- C1/C2: Loeschian representation counts
NL = 200_000
cnt_ab = np.zeros(NL + 1, dtype=np.int32)  # a ≥ b ≥ 0
rA2 = np.zeros(NL + 1, dtype=np.int32)  # all (x, y) in Z^2
lim = math.isqrt(NL) + 2
for b in range(0, lim):
    a = np.arange(b, 2 * lim)
    v = a * a + a * b + b * b
    v = v[v <= NL]
    np.add.at(cnt_ab, v, 1)
xs = np.arange(-2 * lim, 2 * lim + 1)
for x in range(-2 * lim, 2 * lim + 1):
    v = x * x + x * xs + xs * xs
    v = v[(v >= 0) & (v <= NL)]
    np.add.at(rA2, v, 1)
first4 = int(np.argmax(cnt_ab == 4))
firstge4 = int(np.argmax(cnt_ab[1:] >= 4)) + 1
reps = [(a, b) for b in range(0, 42) for a in range(b, 42) if a * a + a * b + b * b == A]
report("C1", first4 == A and firstge4 == A,
       f"smallest n with exactly 4 reps a^2+ab+b^2 (a≥b≥0): {first4}; with ≥4: {firstge4}; reps of 1729: {reps}")
seq = [int(np.argmax(cnt_ab[1:] >= k)) + 1 for k in range(1, 7)]
print(f"     least n with ≥k Loeschian reps, k=1..6: {seq}")
r48 = int(np.argmax(rA2[1:] >= 48)) + 1
report("C2", r48 == A, f"smallest n with ≥48 hexagonal-lattice points on x^2+xy+y^2=n: {r48} (r(1729)={rA2[A]}, N={NL:,})")
rec, best = [], 0
for n in range(1, NL + 1):
    if rA2[n] > best:
        best = rA2[n]
        rec.append(n)
print(f"     record-setters of r_A2(n): {rec[:12]}")

# ---------------------------------------------------------------- C11: centered cube ∩ dodecagonal
both = []
for k in range(0, 1_000_000):
    n = k ** 3 + (k + 1) ** 3
    s = 16 + 20 * n
    t = math.isqrt(s)
    if t * t == s and (4 + t) % 10 == 0:
        both.append(n)
report("C11", len(both) > 1 and both[1] == A, f"numbers both centered-cube and 12-gonal (k<10^6, n<2e18): {both}")

# ---------------------------------------------------------------- controls expected to FAIL (record)


def phi_n(n):
    f = factor(n)
    return math.prod((p - 1) * p ** (e - 1) for p, e in f.items())


def lam_n(n):
    f = factor(n)
    parts = []
    for p, e in f.items():
        if p == 2 and e >= 3:
            parts.append(2 ** (e - 2))
        else:
            parts.append((p - 1) * p ** (e - 1))
    return math.lcm(*parts)


r = next(n for n in range(4, 10 ** 6) if not is_prime[n] and ((n - 1) ** 2) % phi_n(n) == 0)
report("C16", r == A, f"smallest composite n with phi(n) | (n-1)^2: {r}")
r = next(n for n in range(3, 10 ** 6, 2) if not is_prime[n] and all(e == 1 for e in factor(n).values())
         and phi_n(n) == lam_n(n) ** 2)
report("C17", r == A, f"smallest odd squarefree composite n with phi(n)=lambda(n)^2: {r}")
print(f"# runtime {time.time() - T0:.1f}s")
