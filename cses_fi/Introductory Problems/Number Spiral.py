def main():
    x,y=map(int,input().split())
    mx = 0
    my = 0
    # x,y = y,x
    if x % 2:
        mx = (x - 1) ** 2 + 1
    else:
        mx = x * x
    if y % 2 == 0:
        my = (y - 1) ** 2 + 1
    else:
        my = y * y
    if x>y:
        if x%2 == 0:
            print(mx - y + 1)
        else:
            print(mx + y - 1)
    else:
        if y%2:
            print(my - x + 1)
        else:
            print(my + x - 1)
    
 
 
 
 
t = int(input())
for i in range(t):
    main()
