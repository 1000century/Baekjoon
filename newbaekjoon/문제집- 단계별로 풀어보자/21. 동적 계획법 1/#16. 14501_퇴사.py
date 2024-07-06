"""
1차원리스트로 풀었음
"""
N = int(input())
X = [[0,0]]
for _ in range(N):
	X.append(list(map(int,input().split())))

dp = [0]*(N+1)

for i in range(1,N+1): # 일 번호 = i
	duration,profit = X[i][0],X[i][1]
	for j in range(i,N+1): # 퇴사날짜 = j
		if j >= i+duration-1:
			dp[j] = max(dp[i-1]+profit,dp[j])
print(dp[-1])