from math import isqrt

def pf(x):
    f = {}
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            f[i] = 0
            while x % i == 0:
                f[i] += 1
                x //= i
    if x > 1:
        f[x] = 1
    return f

def cf(n, p):
    c = 0
    while n > 0:
        c += n // p
        n //= p
    return c

def ch(n, a):  
    if a == 0:
        return "NO"
    if a == 1:
        return "YES"
    
    f = pf(a)
    for p, e in f.items():
        if cf(n, p) < e:
            return "NO"
    return "YES"

# Input
n, a = map(int, input().split())
print(ch(n, a))
