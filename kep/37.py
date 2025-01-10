a,b,c = map(int,input().split())

dic = {}
dic[a] = 1

if b in dic:
    dic[b] += 1
else:
    dic[b] = 1

if c in dic:
    dic[c] += 1
else:
    dic[c] = 1

mn,mx = a, dic[a]
f = a
for x,y in dic.items():
    mn = min(mn,x)
    if mx < dic[x]:
        mx = dic[x]
        f = x
if mx > 1:
    print(f)
else:
    print(mn)