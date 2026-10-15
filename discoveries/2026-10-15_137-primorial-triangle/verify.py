"""Verify candidate questions whose answer is 137.

Run from the repo root:
    .venv/bin/python discoveries/2026-10-15_137-primorial-triangle/verify.py
"""
from math import gcd, isqrt
from fractions import Fraction
from sympy import primerange, primorial, isprime, n_order, euler, factorint
from sympy.functions.combinatorial.numbers import stirling


def report(cid, ok, msg):
    print(f"{cid}: {'PASS' if ok else 'FAIL'} — {msg}")


# ---- primitive Pythagorean triples (PPTs), complete for hypotenuse < M^2 ----
M = 3400  # c = m^2 + n^2 > m^2, so m < M covers every PPT with c < M^2
CMAX = M * M
tri = []
for m in range(2, M):
    for n in range(1 + (m % 2), m, 2):  # opposite parity
        if gcd(m, n) == 1:
            a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
            tri.append((c, min(a, b), max(a, b), a * b // 2, a + b + c))
tri.sort()
print(f"PPTs enumerated: {len(tri)} (complete for c < {CMAX})")


def min_hyp(pred):
    return next((t for t in tri if pred(t) and t[0] < CMAX), None)


def min_area(pred):
    return min((t for t in tri if pred(t)), key=lambda t: t[3])


# C1: smallest hypotenuse of a PPT whose area is divisible by every prime <= 11
t = min_hyp(lambda t: t[3] % 2310 == 0)
report("C1", t is not None and t[:3] == (137, 88, 105), f"min hyp with 11#=2310 | area: {t}")

# C1-seq: the whole primorial family
seq = [min_hyp(lambda t, P=primorial(k): t[3] % P == 0) for k in range(1, 10)]
print("  min-hyp sequence k=1..9:", [s[0] for s in seq])
print("  triangles (c, a, b, area, perimeter):", seq)
print("  prime hypotenuses:", [isprime(s[0]) for s in seq])

# C2: is the smallest-AREA PPT with 2310 | area the 137 triangle?
t2 = min_area(lambda t: t[3] % 2310 == 0)
report("C2", t2[0] == 137, f"min-area triangle with 2310 | area: {t2}")

# C2b: 11# is the first primorial where the min-hyp and min-area triangles differ.
diff = []
for k in range(1, 10):
    P = primorial(k)
    a = min_hyp(lambda t: t[3] % P == 0)
    b = min_area(lambda t: t[3] % P == 0)
    if a != b:
        diff.append((k, a[0], b[0]))
report("C2b", bool(diff) and diff[0][:2] == (5, 137), f"k where min-hyp != min-area: {diff}")
# Min-area completeness: a PPT with m >= M has area = mn(m-n)(m+n) >= M^3 - M (n = 1),
# which exceeds every min area found, so the min-area answers are exact.
print("  min-area bound check: M^3-M =", M**3 - M, "> max area found =",
      max(min_area(lambda t, P=primorial(k): t[3] % P == 0)[3] for k in range(1, 10)))

# C3: smallest PPT hypotenuse with 2310 | perimeter
t3 = min_hyp(lambda t: t[4] % 2310 == 0)
report("C3", t3[0] == 137, f"min hyp with 2310 | perimeter: {t3}")

# C4: 77 | area alone
t4 = min_hyp(lambda t: t[3] % 77 == 0)
report("C4", t4[0] == 137, f"min hyp with 77 | area: {t4}")

# C5: 35 | area and 11 | area separately trivial; check 5*11 | area
t5 = min_hyp(lambda t: t[3] % 385 == 0)
report("C5", t5[0] == 137, f"min hyp with 5*7*11=385 | area: {t5} (equivalent to C1 since 6 | every PPT area)")

# C6: smallest PPT with leg product divisible by every prime <= 11 (2310 | ab)
t6 = min_hyp(lambda t: (t[1] * t[2]) % 2310 == 0)
report("C6", t6[0] == 137, f"min hyp with 2310 | ab: {t6}")

# C7: smallest prime p = 1 mod 8 with ord_p(10) = 8
p7 = next(p for p in primerange(7, 10**4) if p % 8 == 1 and n_order(10, p) == 8)
report("C7", p7 == 137, f"smallest p = 1 mod 8 with decimal period 8: {p7}")

# C8: smallest Euler-irregular prime (p | E_2k, 2 <= 2k <= p-3) with p = 1 mod 8
E = {n: int(euler(n)) for n in range(2, 300, 2)}
eirr = [p for p in primerange(3, 290) if any(E[n] % p == 0 for n in range(2, p - 2, 2))]
print("  E-irregular primes < 290:", eirr)
p8 = next(p for p in eirr if p % 8 == 1)
report("C8", p8 == 137, f"smallest E-irregular prime = 1 mod 8: {p8}")

# C9: first harmonic numerator that is a prime = 1 mod 4
H = Fraction(0)
found = None
for n in range(1, 200):
    H += Fraction(1, n)
    if H.numerator % 4 == 1 and isprime(H.numerator):
        found = (n, H.numerator)
        break
report("C9", found == (5, 137), f"first prime numerator of H_n with p = 1 mod 4: {found}")


# C10: smallest prime p = 1 mod 8 with h(-4p) = 8
def h(D):
    c, a = 0, 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                cc = (b * b - D) // (4 * a)
                if cc >= a and not (b < 0 and a == cc) and gcd(gcd(a, abs(b)), cc) == 1:
                    c += 1
        a += 1
    return c


p10 = next(p for p in primerange(3, 10**4) if p % 8 == 1 and h(-4 * p) == 8)
report("C10", p10 == 137, f"smallest p = 1 mod 8 with h(-4p) = 8: {p10}")


# C11: smallest prime of every form x^2 + n y^2, n in {1, 2, 7, 8, 16, 32}
def rep(p, n):
    return any(isqrt(p - n * y * y) ** 2 == p - n * y * y for y in range(1, isqrt(p // n) + 1))


p11 = next(p for p in primerange(3, 10**4) if all(rep(p, n) for n in (1, 2, 7, 8, 16, 32)))
report("C11", p11 == 137, f"smallest prime of forms n = 1,2,7,8,16,32: {p11}")


# C12: smallest prime 2^7 + 2^b + 1 whose GF(2) trinomial x^7 + x^b + 1 is primitive
def primitive_trinomial(a, b):
    poly, N = (1 << a) | (1 << b) | 1, (1 << a) - 1

    def mulmod(x, y):
        r = 0
        while y:
            if y & 1:
                r ^= x
            y >>= 1
            x <<= 1
            if x >> a & 1:
                x ^= poly
        return r

    def pw(e):
        r, x = 1, 2
        while e:
            if e & 1:
                r = mulmod(r, x)
            x = mulmod(x, x)
            e >>= 1
        return r

    return pw(N) == 1 and all(pw(N // q) != 1 for q in factorint(N))


c12 = [(1 << 7) + (1 << b) + 1 for b in range(1, 7)
       if primitive_trinomial(7, b) and isprime((1 << 7) + (1 << b) + 1)]
report("C12", bool(c12) and c12[0] == 137, f"prime 2^7+2^b+1 with primitive trinomial: {c12}")

# C13: smallest prime > 100 that is not a sum of >= 2 consecutive primes
ps = list(primerange(2, 3000))
sums = set()
for i in range(len(ps)):
    s = ps[i]
    for j in range(i + 1, len(ps)):
        s += ps[j]
        if s > 3000:
            break
        sums.add(s)
nots = [p for p in ps if p not in sums]
print("  primes < 300 not a sum of >= 2 consecutive primes:", [p for p in nots if p < 300])
p13 = next(p for p in nots if p > 100)
report("C13", p13 == 137, f"smallest prime > 100 not a consecutive-prime sum: {p13}")

# C14: |s(6,2)| = 274 = 2*137 (unsigned Stirling, first kind) — a restatement of H_5
report("C14", stirling(6, 2, kind=1) == 274, f"|s(6,2)| = {stirling(6, 2, kind=1)} (KNOWN restatement)")

# C15: smallest prime p > 100 with x^2 + 1 = 10p
p15 = next((x * x + 1) // 10 for x in range(1, 10**4)
           if (x * x + 1) % 10 == 0 and isprime((x * x + 1) // 10) and (x * x + 1) // 10 > 100)
report("C15", p15 == 137, f"smallest prime p > 100 with x^2+1 = 10p: {p15}")
