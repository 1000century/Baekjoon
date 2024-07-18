# 풀었는데 뭔가 이해가 안되지?
# (세현)

dp = [0]*10001

for i in [1,2,3]:
	dp[i] = dp[i] + 1
	for j in range(i,10001):
		dp[j] = dp[j] + dp[j-i]

T = int(input())
for _ in range(T):
	x = int(input())
	print(dp[x])