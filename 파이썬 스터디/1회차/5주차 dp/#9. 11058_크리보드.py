"""
dp는 귀찮아도 한번씩 다 생각해보기는 해야겠다.
처음부터 다 해봤으면 얼마 안 걸렸을텐데 딴짓하다가 1시간 걸림
"""


dp = [0]*101
for i in range(0,6):
	dp[i] = i
for n in range(6,101):
	dp[n] = max(dp[n-5]*4, dp[n-4]*3, dp[n-3]*2)


N = int(input())
print(dp[N])