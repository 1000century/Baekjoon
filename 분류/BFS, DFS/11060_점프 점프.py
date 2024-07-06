N = int(input())
A = list(map(int,input().split()))

INF = int(1e9)
dp = [INF] * (N)
dp[0] = 0
for i in range(N):
	for j in range(1,A[i]+1):
		if i+j<N:
			dp[i+j] = min(dp[i+j],dp[i] + 1)

if dp[i] ==INF:
	print(-1)
else:
	print(dp[-1])
