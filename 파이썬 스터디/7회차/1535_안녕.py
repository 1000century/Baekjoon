N = int(input())
체력 = [0]+list(map(int,input().split()))
해피 = [0]+ list(map(int,input().split()))


dp = [0]*100
for i in range(1,N+1):
	h, d = 체력[i],해피[i]
	temp = [0]*100
	for ch in range(0,100):
		temp[ch] = dp[ch]
		if ch-h<0:
			if ch ==0:
				temp[ch] = dp[ch]
			else:
				temp[ch] = max(dp[ch],temp[ch-1])
		else:
			if ch == 0:
				temp[ch] = max(dp[ch-h]+d,dp[ch])
			else:
				temp[ch] = max(dp[ch-h]+d,temp[ch-1],dp[ch])
	dp = temp[:]
print(dp[-1])
