res = []

for i in range(1, int(input()) + 1):
    res.extend([i] * ((i % 3) if i % 3 else 3))
print(*res)
