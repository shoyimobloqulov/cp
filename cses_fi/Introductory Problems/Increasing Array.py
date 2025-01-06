n = int(input())
r = list(map(int,input().split()))
cnt = 0
for i in range(1,n):
    if r[i]<r[i-1]:
        cnt += abs(r[i]-r[i-1])
        r[i]+=abs(r[i]-r[i-1])
        
print(cnt)
