n = int(input())
r = [i for i in range(1, n + 1)]
s = (n * (n + 1)) // 2
 
if s % 2:
    print("NO")
else:
    hs = s // 2
    print("YES")
    i = n
    t = []
    while hs != 0:
        if i <= hs:
            hs -= i
            t.append(i)
            r[i - 1] = 0 
        i -= 1
 
    t.sort()
    print(len(t))
    print(*t)  
    r = [x for x in r if x != 0] 
    print(len(r))
    print(*r)
