# (세현)

N, K = map(int,input().split())

dp = [1]*(N+1)
for i in range(1,K):
	temp =dp[:]
	for j in range(N+1):
		for k in range(j):
			temp[j] = (temp[j] + dp[k])%1000000000
	dp = temp[:]
print(dp[-1]%1000000000)
