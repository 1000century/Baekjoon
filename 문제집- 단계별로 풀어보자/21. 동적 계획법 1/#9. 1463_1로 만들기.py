"""
def three(N):
	if dp[N]:
		return dp[N]
	if N % 3 ==0:
		return three(N//3)
	if N % 2 ==0:
		return three(N//2)
	return three(N-1)
print(three(30))
"""
# (세현)
N = int(input())

dp = [0] * 1000001
dp[1] = 0

for i in range(2,N+1):
	if dp[i]!=0:
		continue
	else:
		dp[i] = dp[i-1] + 1
		if i%3 == 0:
			dp[i] = min(dp[i],dp[i//3] + 1)
		if i%2 == 0:
			dp[i] = min(dp[i],dp[i//2] + 1)
print(dp[N])
