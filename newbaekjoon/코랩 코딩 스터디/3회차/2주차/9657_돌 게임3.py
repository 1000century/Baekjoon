N = int(input())
dp =[0]*(1001)

dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "SK"
for i in range(5, 1001):
	if not (dp[i-1] == dp[i-3] == dp[i-4] == "SK"):
		dp[i] = "SK"
	else:
		dp[i] = "CY"
print(dp[N])