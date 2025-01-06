n,m,k = map(int,input().split())
r = sorted(map(int,input().split()))
o = sorted(map(int,input().split()))
j = 0
i = 0
cnt = 0
while i < n and j < m:
    if abs(r[i]-o[j])<=k:
        cnt+=1
        i+=1
        j+=1
    else:
        if r[i]-o[j]>k:
            j+=1
        else:
            i+=1
print(cnt)
