n = int(input())
X = [0]

dp = [[0,0] for _ in range(n+1)]
for _ in range(n):
	X.append(int(input()))

if n == 1:
	print(X[1])
	quit()

dp[1] = [X[1],X[1]] # 다음턴에 두 경우 모두 마쉴 수는 있음
dp[2] = [X[2], X[1]+X[2]]  # 다음 턴에 한 경우만 마실 수 있음

#print(*dp,sep='\n')
#print(X)

for i in range(3,n+1):
	# 이번에 마심 - 이번에만 마시는 경우
	dp[i][0] = max(max(dp[i-3]), max(dp[i-2])) + X[i]
    # 이번에 마심 - 두 번 연달아 마심 (다음 번에 못 마심)
	dp[i][1] = dp[i-1][0]+X[i]

print(max(max(dp[-1]),max(dp[-2]),max(dp[-3])))