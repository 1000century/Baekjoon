"""
암호코드
https://www.acmicpc.net/problem/2011
"""
def solution(nums):
	if nums[0] == 0:
		return 0
	code = [0]+list(map(int,nums.replace(""," ").split()))

	dp = [0]*(len(code))
	dp[0] = 1

	for i in range(1,len(code)):
		if code[i] == 0 and (code[i-1] ==0 or code[i-1]>2):
			return 0

		if code[i] != 0:
			dp[i] = dp[i-1]
		if i == 1:
			continue
		if (code[i-1] ==1) or (code[i-1] == 2 and code[i]<=6):
			dp[i] = dp[i] + dp[i-2]

	return dp[-1]%1000000
	
nums = str(input())
print(solution(nums))
