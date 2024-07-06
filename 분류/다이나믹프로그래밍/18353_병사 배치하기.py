"""
11053_가장 긴 증가하는 부분수열
일단 dp[i] == dp[j]를 넣는 것보다는 max로 크기비교하는 게 정석인듯
근데 크기비교하게 되면 시간이 더 증가됨
"""

N = int(input())
X = [0] + list(map(int,input().split()))

dp = [1] * (N+1)

for i in range(1,N+1):
	for j in range(i,N+1):
		now = X[i]
		next = X[j]
		if now > next: # 서있는 것이 조건에 맞는다면
			dp[j] = max(dp[j],dp[i] + 1)
print(N- max(dp))