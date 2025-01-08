n = int(input())
l = list(map(int, input().split()))
t = int(input())

dic = {}

for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

s = 0
for _ in range(t):
    x = int(input())
    if x in dic:
        s += dic[x]
print(s)
