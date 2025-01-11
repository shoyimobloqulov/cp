def s(n):
    return sum(int(d) for d in str(n))

x = int(input())
y = int(input())

k = 1
while k <= x:
    if x - k == s(y + k):
        print(k)
        break
    k += 1
else:
    print(-1)
