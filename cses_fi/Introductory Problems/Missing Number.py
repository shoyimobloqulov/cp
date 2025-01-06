n = int(input())
r = sorted(map(int,input().split()))
for i in range(1,n+1):
    if n==i:
        print(i)
        quit()
    if i!=r[i-1]:
        print(i)
        quit()
