import math

g,l = map(int,input().split())

res = l * g

for a in range(g, res + 1, g):
    b = res // a
    if math.gcd(a, b) == g and (a * b == res):
        print(f"{a} {b}")
        exit(0)
print(-1)