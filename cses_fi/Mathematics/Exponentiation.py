n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    print(pow(a,b,int(1e9+7)))
