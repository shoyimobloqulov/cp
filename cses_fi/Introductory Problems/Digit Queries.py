def func(k):
    d, c, p = 1, 9, 1
    while k > d * c:
        k -= d * c
        d += 1
        c *= 10
        p *= 10
    n = p + (k - 1) // d
    return int(str(n)[(k - 1) % d])

q = int(input())
for _ in range(q):
    k = int(input())
    print(func(k))
