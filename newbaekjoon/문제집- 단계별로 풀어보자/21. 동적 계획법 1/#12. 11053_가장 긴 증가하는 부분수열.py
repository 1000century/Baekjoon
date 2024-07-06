"""
이걸 이분탐색으로 풀면 시간단축 됨

18353_병사배치하기 참고
"""

import sys

N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

dp = [1]*N
for i in range(N):
	now = X[i]
	for j in range(i+1,N):
		next= X[j]
		if next>now and dp[i]==dp[j]:
			dp[j] = dp[j] + 1
print(max(dp))



