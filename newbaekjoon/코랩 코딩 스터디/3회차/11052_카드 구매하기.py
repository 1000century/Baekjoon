# (세현) 왜맞음? 

N = int(input())
P곤 = [0]+list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
	for j in range(1,i+1):
		dp[i] = max(dp[i], P곤[j]+dp[i-j])

print(dp[-1])