# (세현)

N = int(input())
X = list(map(int,input().split()))
dp = [0]*(N)
for idx, i in enumerate(X):
	if idx ==0:
		dp[idx] = i
		continue
	dp[idx] = dp[idx-1]+i
ans = 0

# 벌통이 오른쪽 끝에 있는 경우 (한쪽벌은 왼쪽 끝 고정)
rt = []
for i in range(1,N-1):
	rt.append(2*dp[N-1]-X[0]-dp[i]-X[i])

# 벌통이 왼쪽 끝에 있는 경우 (한쪽 벌은 오른쪽 끝 고정)
lt = []
for i in range(1,N-1):
	lt.append(dp[i-1]+dp[-2]-X[i])

# 벌통이 가운데 있는 경우(벌이 양끝에서 출밟)
mid = []
for i in range(1,N-1):
	mid.append(dp[N-2]-dp[0]+X[i])

print(max(max(mid),max(rt),max(lt)))
