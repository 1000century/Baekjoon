n = int(input())
dp = [0]*(n+2) # n=0 일때 때문에 n+1이 아니라 n+2

dp[0] = 0
dp[1] = 1
for i in range(2,n+2):
	dp[i] = dp[i-1]+dp[i-2]
print(dp[n+1]*2 + dp[n]*2)