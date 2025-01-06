mod = 10**9 + 7
n = 10**6 + 1
fc = [1] * n
for i in range(1, n):
    fc[i] = (fc[i - 1] * i) % mod
 
def inv(x, m):
    return pow(x, m - 2, m)
 
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        print(0)
    else:
        r = fc[a]
        r = r * inv(fc[b], mod) % mod
        r = r * inv(fc[a - b], mod) % mod
        print(r)
