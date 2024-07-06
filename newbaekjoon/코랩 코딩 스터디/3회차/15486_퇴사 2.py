# (세현) 

import sys
input = sys.stdin.readline

N = int(input())
days = [[] for _ in range(N+1)]

for i in range(N):
	t,p = map(int,input().split())
	if i+t<=N:
		days[i+t].append([i,p])
dp = [0]*(N+1)
for i in range(1,N+1):
	dp[i] = dp[i-1]
	for j,p in days[i]:
		dp[i] = max(dp[i],dp[j]+p)
print(dp[-1])