import math

def a(n):
    m = math.isqrt(n)
    return math.floor(m * (n - m**2 / 3 - m / 2 + 5 / 6)+0.1)

n = int(input())
print(a(n))
2