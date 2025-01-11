import math

def solve(n):
    count = 0
    for x in range(1, int(math.sqrt(n)) + 1):
        max_y = int(math.sqrt(n - x**2))
        count += max_y
    return count

n = int(input())

print(solve(n))
