def f(k):
    a1 = 2 ** (1 / k)
    p = a1
    m = 1

    while True:
        m += 1
        an = a1 ** (2 ** (m - 1))
        p *= an

        if p.is_integer():
            return m
        if m > k:
            return -1

k = int(input())
r = f(k)
print(r)
