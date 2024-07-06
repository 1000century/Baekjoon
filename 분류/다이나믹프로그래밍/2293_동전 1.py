# (세현)

n,k = map(int,input().split())

X = [0]
for _ in range(n):
	X.append(int(input()))
dp = [0]*(k+1)
dp[0] = 1

for i in range(1,n+1):
	for j in range(X[i],k+1):		
		dp[j] = dp[j] + dp[j-X[i]] # 현재 동전

print(dp)