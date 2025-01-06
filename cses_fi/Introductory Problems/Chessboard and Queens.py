def func(b, r, c, p, q, a):
    if r == 8:
        a[0] += 1
        return
    for i in range(8):
        if b[r][i] == '*' or c[i] or p[r - i + 8] or q[r + i]:
            continue
        c[i] = p[r - i + 8] = q[r + i] = True
        func(b, r + 1, c, p, q, a)
        c[i] = p[r - i + 8] = q[r + i] = False

b = [input() for _ in range(8)]
c = [False] * 10
p = [False] * 20
q = [False] * 20
a = [0]

func(b, 0, c, p, q, a)
print(a[0])
