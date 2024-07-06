N = int(input())

dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
	dp[i] = dp[i-1] + dp[i-2]
print(dp[N])

# ~1 0   ~0 0 >>> dp[N-1]
# ~0 1 === ~001 ~101 >>>> dp[N-2]