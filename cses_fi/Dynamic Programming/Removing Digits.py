n = int(input())
dp=[0]*(n+1)
for i in range(1,min(10,n+1)):dp[i]=1
for i in range(10,n+1):
    mx = max([int(j) for j in str(i)])
    dp[i] = 1+dp[i-mx]
print(dp[n])
