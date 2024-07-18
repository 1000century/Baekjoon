# (세현)

import sys
input = sys.stdin.readline
N,K,Q,M = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
dp =[0]*(N+3)

for i in y:
	cnt = 0
	if i in x:
		continue
	while i*(1+cnt) <N+3:
		cnt = cnt + 1
		if i*cnt not in x:
			dp[i*cnt] = 1
for i in range(1,len(dp)):
	dp[i] = dp[i] + dp[i-1]
for _ in range(M):
	S,E = map(int,input().split())
	print(E-S+1-dp[E]+dp[S-1])