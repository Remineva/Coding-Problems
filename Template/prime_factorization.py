#linear_sieve, return the first n primes
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]

#Miller-Rabin
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in L:
        return True
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return False
            t <<= 1
    return True
 
#Pollard-Rho, return a nontrivial factor
def findFactorRho(n):
    from math import gcd
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)
 
#return a dictionary of factorization
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = False
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = True
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret

# get the smallest factor
import math
MAXN = 100
spf = [0 for i in range(MAXN)]
def sieve():
	spf[1] = 1
	for i in range(2, MAXN):
		spf[i] = i
	for i in range(4, MAXN, 2):
		spf[i] = 2
	for i in range(3, math.ceil(math.sqrt(MAXN))):
		if (spf[i] == i):
			for j in range(i * i, MAXN, i):
				if (spf[j] == j):
					spf[j] = i
sieve()
# get the distinct factors
def getFactorization(x):
	ret = []
	while x != 1:
		if ret:
			if spf[x] != ret[-1]:
				ret.append(spf[x])
		else:
			ret.append(spf[x])
		x = x // spf[x]
	return ret

