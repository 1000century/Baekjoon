import sys

N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

dp = [1]*N
for i in range(N):
	now = X[i]
	for j in range(i+1,N):
		next= X[j]
		if next>now and dp[i]==dp[j]:
			dp[j] = dp[j] + 1
bdp = [1]*N
for i in range(N-1,-1,-1):
	now = X[i]
	for j in range(i-1,-1,-1):
		next= X[j]
		if next>now and bdp[i]==bdp[j]:
			bdp[j] = bdp[j] + 1

ans = 0
for i in range(N):
	ans = max(ans,dp[i] + bdp[i]-1)
print(ans)
