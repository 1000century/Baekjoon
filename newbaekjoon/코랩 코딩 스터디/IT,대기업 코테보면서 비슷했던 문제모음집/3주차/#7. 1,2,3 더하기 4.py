
dp = [0]*(10000+1)

for i in [1,2,3]:
	dp[i] = dp[i] + 1
	for j in range(i,10001):
		dp[j] = dp[j] + dp[j-i]



"""
dp[1],dp[2],dp[3] = 1,2,3
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
"""

n = int(input())
for i in range(n):
	x = int(input())
	print(dp[x])
