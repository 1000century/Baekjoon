# (세현)
N = int(input())

X=[[0,0]]

for _ in range(N):
	X.append(list(map(int,input().split())))

dp = [[0]*(N+1) for _ in range(N+1)] # 2차원 리스트

# 점화식 dp[i][j]
# 해당 일을 물리적으로 못하는 경우: dp[i][j-1] or dp[i-1][j]
# 해당 일을 할 수 있는 경우: dp[i][j-1] or dp[i][j-1] or dp[i-1][j-t]+p
# dp[i][j-1]: 어제 퇴사한 경우
# dp[i-1][j]: 오늘 퇴사 + 이번 일 받기 전까지의 최대 의 경우
# dp[i-1][j-1]+ p : 이번 일을 하는 경우

ans = 0

for i in range(N+1):
	for j in range(N+1):
		t, p = X[i][0], X[i][1]
		if i+t-1>j:
			dp[i][j] = max(dp[i][j-1], dp[i-1][j])
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][i-1]+p)

		ans = max(ans,dp[i][j])
print(ans)