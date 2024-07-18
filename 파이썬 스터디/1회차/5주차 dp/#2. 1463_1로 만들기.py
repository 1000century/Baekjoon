N = int(input())

dp =[0] * (1000001)
dp[1] = 0


for i in range(2,N+1):
	temp = []

	# 4 = 1+1+1+1
	temp.append(dp[i-1] + 1)

	# 4 >> temp [dp[2]+1]
	if i % 2 == 0:
		temp.append(dp[i//2]+1)	

	# 4 3으로 안나눠떨어지니까
	if i % 3 == 0:
		temp.append(dp[i//3]+1)
	
	# min ( temp= [dp[3] + 1, dp[2]+1], dp[i//3]+1)
	dp[i] = min(temp)

print(dp[N])

