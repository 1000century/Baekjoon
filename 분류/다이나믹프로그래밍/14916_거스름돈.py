n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
dp[0] = 0

A = [2,5]
"""
for coin in A:
	for i in range(coin,n+1):
		dp[i] = dp[i]+dp[i-coin]
	print("COIN",coin,dp)
print(dp)
"""

for coin in A:
	if coin > n:
		continue
	if dp[coin] != INF:
		dp[coin] = dp[coin] + 1
	for i in range(coin,n+1):
		dp[i] = min(dp[i-coin] + 1,dp[i])
if dp[-1] == INF:
	print(-1)
else:
	print(dp[-1])