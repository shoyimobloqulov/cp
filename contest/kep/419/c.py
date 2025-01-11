n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
s = [sum(r) for r in p]
m = max(s)
print("Yes" if s.count(m) == 1 else "No")
