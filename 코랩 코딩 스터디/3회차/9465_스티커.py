# (세현)

import sys
input = sys.stdin.readline
def solution():
	n = int(input())
	A  = [[0]+list(map(int,input().split())) for _ in range(2)]
	dp = [[0]*(n+1) for _ in range(2)]
	dp[0][1] = A[0][1]
	dp[1][1] = A[1][1]

	for i in range(2,n+1):
		temp = max(dp[0][i-2],dp[1][i-2])
		for j in range(2):
			dp[j][i] = A[j][i]+max(dp[1-j][i-1],temp)
	
	ans = max(dp[0][-1],dp[1][-1])
	if n>=2:
		ans = max(ans, max(dp[0][-2],dp[1][-2]))
	print(ans)

for _ in range(int(input())):
	solution()