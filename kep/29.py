def qs(a, l, r, k):
    if l == r:
        return a[l]

    p = pt(a, l, r)

    if k == p:
        return a[k]
    elif k < p:
        return qs(a, l, p - 1, k)
    else:
        return qs(a, p + 1, r, k)

def pt(a, l, r):
    pv = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= pv:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(qs(a, 0, n - 1, k - 1))
