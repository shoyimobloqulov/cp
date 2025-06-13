mod = 10**9+7
n = int(input())
ar = [input() for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in reversed(range(n)):
    for j in reversed(range(n)):
        if ar[i][j] == "*":
            dp[i][j] = 0
        elif i == n-1 and j == n-1:
            dp[i][j] = 1
        else:
            if i+1 < n:
                dp[i][j] += dp[i+1][j]
            if j+1 < n:
                dp[i][j] += dp[i][j+1]
            dp[i][j] %= mod
# for i in dp:
#     print(dp)
print(dp[0][0])
