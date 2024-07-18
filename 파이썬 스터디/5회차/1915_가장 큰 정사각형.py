n,m = map(int,input().split())
arr = [[0]*(m+1)] + [[0]+list(map(int, input().replace('',' ').split())) for _ in range(n)]
dp = [[0]*(1+m) for _ in range(n+1)]
ans = 0
for i in range(1, n + 1):
	for j in range(1, m + 1):
		if arr[i][j]:
			dp[i][j] = 1
			if arr[i - 1][j] and arr[i][j - 1] and arr[i - 1][j - 1]:
				dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
			ans = max(ans, dp[i][j])

print(ans * ans)