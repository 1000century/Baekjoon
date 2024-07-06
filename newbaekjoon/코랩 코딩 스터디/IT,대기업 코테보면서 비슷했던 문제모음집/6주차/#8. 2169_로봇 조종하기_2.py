# (세현)

# O(N**3)이면 절대 안 풀림.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 첫번째 행
dp = list(map(int, input().split()))
for i in range(1,M):
	dp[i] = dp[i-1]+dp[i]

# 나머지 행
for _ in range(N - 1):
	current_row = list(map(int, input().split()))
	top = dp[:]
	right = current_row[:]
	left = current_row[:]

	# 위쪽
	for j in range(M):
		top[j] = top[j]+current_row[j]
	
	# 왼쪽 >> 위쪽에서 내려온 경우 & 왼쪽에서 온 경우 중 최대값
	left[0] = top[0]
	for j in range(1,M):
		left[j] = max(top[j-1],left[j-1]) + current_row[j]
	
	# 오른쪽 >> 위쪽에서 내려온 경우 * 오른족에서 온 경우 중 최대값
	right[-1] = top[-1]
	for j in range(M-2,-1,-1):
		right[j] = max(top[j+1],right[j+1])+current_row[j]
	
	# 위쪽. 왼쪽, 오른쪽에서 오는 경우 중 최대값 찾기
	for i in range(M):
		dp[i] = max(top[i],left[i],right[i])

print(dp[-1])