n = int(input())
w = list(map(int, input().split()))
 
mn = 1e10
for i in range(1 << n):
    g1 = g2 = 0
    for j in range(n):
        if i & (1 << j):
            g1 += w[j]
        else:
            g2 += w[j]
    mn = min(mn, abs(g1 - g2))
 
print(mn)
