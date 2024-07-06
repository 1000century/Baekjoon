# (세현)
N = int(input())
dp = [0,1]
for i in range(2,N+1):
	if dp[i-1] == 1:
		dp.append(0)
	else:
		dp.append(1)
if dp[N] == 1:
	print("SK")
else:
	print("CY")