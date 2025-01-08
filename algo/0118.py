n = int(input())
l = list(map(int,input().split()))
k = 0
s = 0
for i in l:
    if i % 2 == 1:
        s += i
        k += 1
print("%0.2f" % (s / k + 0.0001))