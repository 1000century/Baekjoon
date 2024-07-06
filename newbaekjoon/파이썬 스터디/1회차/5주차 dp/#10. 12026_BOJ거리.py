# 가장 긴 증가하는 부분수열 문제랑 느낌이 비슷한듯

N = int(input())
X = [0] + list(input())
dp = [int(1e9)]*(N+1)
dp[0] = 0
dp[1] = 0

for i in range(1,N+1):
	now = X[i]
	
	for j in range(i+1,N+1):
		next = X[j]
		if (now =="B" and next=="O") or (now =="O" and next=="J") or (now =="J" and next=="B"):
			dp[j] = min(dp[j],dp[i] + (j-i)**2)
if dp[-1] == int(1e9):
	print(-1)
else:
	print(dp[-1])
