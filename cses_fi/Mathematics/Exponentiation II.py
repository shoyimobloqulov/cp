n = int(input())
mod = int(1e9+7)
for i in range(n):
    a,b,c = map(int,input().split())
    print(pow(a,pow(b,c,int(mod-1)),mod))
