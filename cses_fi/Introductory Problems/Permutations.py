n = int(input())
if n==3 or n==2:
    print("NO SOLUTION")
    quit()
if n==4:
    print(*[2,4,1,3])
    quit()
print(*[[i for i in range(1,n+1,2)]+[i for i in range(2,n+1,2)]][0])
