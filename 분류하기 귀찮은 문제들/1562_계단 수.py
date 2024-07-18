N = int(input())
dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(N)]
# dp[x][y][z] = 자릿수 x까지 봤을 때, 현재 숫자로 y를 선택한 경우\
# 비트 z에 해당하는 숫자들을 방문했을 때, 경우의 수

for k in range(1,10):
	dp[0][k][1<<k] = 1

for i in range(1,N):
	for k in range(10):
		for bit in range(1<<10):
			# bit | (1 << k) == 이전 방문 기록(bit)에 현재 숫자 방문 기록을 추가(| (1 << k))
			if k>0:
				dp[i][k][bit|(1<<k)] += dp[i-1][k-1][bit]
			if k<9:
				dp[i][k][bit|(1<<k)] += dp[i-1][k+1][bit]
			dp[i][k][bit|(1<<k)] %= int(1e9)

ans = 0
for k in range(10):
	ans = ans + dp[N-1][k][1023]
	ans = ans % int(1e9)
print(ans)