n = int(input())
h = 1
while n!=0:
    n-=1
    h*=2
    h%=int(1e9+7)
print(h)
