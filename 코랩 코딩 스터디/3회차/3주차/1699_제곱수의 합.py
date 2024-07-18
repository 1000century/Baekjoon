# (세현)
N =int(input())
dp =[int(1e9)]*(N+1)
for i in range(1,int(N**0.5)+1):
	dp[i**2] = 1
for i in range(1,N+1):
	if dp[i] ==1:
		continue
	for j in range(1,int(i**0.5)+1):
		dp[i] = min(dp[i],dp[j**2]+dp[i-j**2])
		if dp[i] == 2:
			break

print(dp[N])