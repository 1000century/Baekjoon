# dp > 동전종류 순서 상관없이 조합하기

def solution(N,coin,M):
	dp = [[0]*(M+1) for _ in range(len(coin))]
	for c in range(len(coin)):
		dp[c][0] = 1
		for k in range(1,M+1):
			dp[c][k] = dp[c][k] + dp[c-1][k]
			if k >=coin[c]:
				dp[c][k] = dp[c][k] + dp[c][k-coin[c]]
	return dp[-1][-1]


T = int(input())
for _ in range(T):
	N = int(input())
	coin = list(map(int,input().split()))
	M = int(input())
	print(solution(N,coin,M))