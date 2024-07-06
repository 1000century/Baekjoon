n = int(input())

dp = [0]*10001
dp[0] = 1

for i in [1,2,3]:
	for j in range(i,10001):
		dp[j] = dp[j] + dp[j-i]
for _ in range(n):
	x = int(input())
	print(dp[x])