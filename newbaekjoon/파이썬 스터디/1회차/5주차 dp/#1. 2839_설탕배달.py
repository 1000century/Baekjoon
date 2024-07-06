"""
N = int(input())
a =  N //5
for i in range(a+1):
    if (N - 5*(a-i)) % 3 == 0:
        print(a-i+(N - 5*(a-i)) // 3)
        exit()
print(-1)
"""


N = int(input())

# dp 리스트는 각 무게별로 만들 수 있는 가짓수
dp = [0] * (5001)
dp[3] = 1
dp[5] = 1

# count 리스트는 각 무게를 만들 때 필요한 봉지개수
count = [int(1e9)]*(5001)
count[3] = 1
count[5] = 1

# 동전 먼저 돌리고 무게
for i in [3,5]:
	for j in range(i,N+1):
		dp[j] = dp[j]+dp[j-i]
		count[j] = min(count[j],count[j-i] + 1)

if dp[N] == 0:
	print(-1)
else:
	print(count[N])