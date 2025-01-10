n = int(input())
l = list(map(int,input().split()))
ctn = 2
for i in range(n):
    if l[i] == 1:
        ctn -= 1
    if ctn == 0:
        print(i)
        exit()
print(-1)