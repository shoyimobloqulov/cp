n = input()
cnt = 1
r = [1]
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        cnt+=1
    else:
        r.append(cnt)
        cnt = 1
if cnt!=1:
    r.append(cnt)
print(max(max(r),1))
