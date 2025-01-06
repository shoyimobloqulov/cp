def main():
    a,b = map(int,input().split())
    if (a + b) % 3 == 0 and a <= 2 * b and b <= 2 * a:
        print("YES")
        return 
    print("NO")
    return
 
n = int(input())
for i in range(n):
    main()
