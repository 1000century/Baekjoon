# (세현)
# 제대로 이해하고 푼 건 아님. 그냥 최장 증가하는 수열이다로 푼것뿐..
# dp(LIS) longest increasing 

N = int(input())
li = [int(input()) for _ in range(N)]

dp = [1] *(N)
for i in range(N):
	for j in range(i):
		if li[i] > li[j]:
			dp[i] = max(dp[j]+1,dp[i])
print(N-max(dp))