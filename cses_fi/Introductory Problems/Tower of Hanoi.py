def rec(n, a, b, c, m):
    if n == 0:
        return
    rec(n - 1, a, c, b, m)
    m.append((a, c))
    rec(n - 1, b, a, c, m)
 
n = int(input())
m = []
rec(n, 1, 2, 3, m)
print(len(m))
for x, y in m:
    print(x, y)
