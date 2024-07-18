"""
1학년
https://www.acmicpc.net/problem/5557

시도 1: itertools > product
시도 2: dp
"""

N = int(input())
nums = list(map(int,input().split()))

dp = [0]*21
dp[nums[0]] = 1
for m in range(1,N-1):
	temp = [0]*21
	for i in range(21):
		if dp[i] == 0:
			continue
		if 0<=i + nums[m]<=20:
			temp[i+nums[m]] = temp[i+nums[m]] + dp[i]
		if 0<=i - nums[m]<=20:
			temp[i-nums[m]] = temp[i-nums[m]] + dp[i]

	dp = temp[:]

print(dp[nums[-1]])
