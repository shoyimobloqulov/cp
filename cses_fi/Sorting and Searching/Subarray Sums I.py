def func(n, x, a):
    b, e, s, c = 0, 0, 0, 0
    while e < n:
        s += a[e]
        while b <= e and s > x:
            s -= a[b]
            b += 1
        if s == x:
            c += 1
            s -= a[b]
            b += 1
        e += 1
    return c
n, m = map(int,input().split())
r = list(map(int,input().split()))
print(func(n,m,r))
