# 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int,input().split()))

dp = [1]*N
ans = [[] for _ in range(N)]
for i in range(N):
	now = A[i]
	ans[i].append(now)
	for j in range(i+1,N):
		next= A[j]
		if next>now and dp[i]+1 > dp[j]:
			dp[j] = dp[i] + 1
			ans[j] = ans[i][:]
print(max(dp))
print(*ans[dp.index(max(dp))])