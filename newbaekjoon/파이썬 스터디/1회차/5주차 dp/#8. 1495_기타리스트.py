N,S,M = map(int,input().split()) # 곡 개수, 시작볼륨, M 은 최대 볼륨

X = list(map(int,input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for n in range(1,N+1): # 몇 번째인지
	for j in range(0,M+1): # 각 볼륨이 가능한지
		v = X[n-1]
		if (j-v>=0 and dp[n-1][j-v]):
			dp[n][j] = 1
		elif (j+v<=M and dp[n-1][j+v]):
			dp[n][j] = 1

ans = -1
for i in range(M,-1,-1):
	if dp[N][i] == 1:
		ans = i
		break
print(ans)


"""
아래는 시간단축을 위해 마지막 N-1 번째까지와 N 번째까지를 구분한 것

N,S,M = map(int,input().split()) # 곡 개수, 시작볼륨, M 은 최대 볼륨

X = list(map(int,input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for n in range(1,N): # 몇 번째인지
	for j in range(0,M+1): # 각 볼륨이 가능한지
		v = X[n-1]
		if j-v>=0 and dp[n-1][j-v]:
			dp[n][j] = 1
		elif j+v<=M and dp[n-1][j+v]:
			dp[n][j] = 1

ans = -1
for j in range(0,M+1): # 각 볼륨이 가능한지
	v = X[N-1]
	if j-v>=0 and dp[N-1][j-v]:
		dp[N][j] = 1
		ans = max(ans,j)
	elif j+v<=M and dp[N-1][j+v]:
		dp[N][j] = 1
		ans = max(ans,j)
print(ans)
"""