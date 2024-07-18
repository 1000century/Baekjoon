# 23.03.19 23:52~24:14

T = int(input())
dp =[[0,0,0] for _ in range(41)]
dp[0] = [0,1,0]
dp[1] = [1,0,1]

for i in range(2,41):
	dp[i] = [
		dp[i-1][0]+dp[i-2][0],
		dp[i-1][1]+dp[i-2][1],
		dp[i-1][2]+dp[i-2][2]
	]


for _ in range(T):
	N = int(input())
	print(dp[N][1],dp[N][2])

