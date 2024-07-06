# pypy3로만 통과

import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [int(1e9)] * (1 << N)
#DP[x][visited] = 현재 x번째 사람을 보고 있고 그 전까지 방문한 조합이 visited 일 때의 최솟값. 반대인가?
dp[0] = 0
print(dp)
print()
print()
for bit in range(1 << N): # bit >> 지금까지 어떤 일들이 할당되었는지
	x = 0
	for j in range(N):
		if bit & (1<<j):
			x = x + 1
	for j in range(N): # j >> 누가 일할지
		print(bin(bit),bin(1<<j))
		if not (bit&(1<<j)):
			dp[bit|(1 << j)] = min(dp[bit | (1 << j)], dp[bit] + arr[x][j])
		print(dp)
	print()

print(dp[-1])


"""
3
2 3 3
3 2 3
3 3 2

# 처음엔 아무도 일 안한상태였음
[0,   2,   3, 1000000000, 3, 1000000000, 1000000000, 1000000000] 
 000 001  010     011     100  101          110        111 
[0, 2, 3, 4, 3, 5, 1000000000, 1000000000]
[0, 2, 3, 4, 3, 5, 6, 1000000000]
[0, 2, 3, 4, 3, 5, 6, 6]
[0, 2, 3, 4, 3, 5, 5, 6]
[0, 2, 3, 4, 3, 5, 5, 6]
[0, 2, 3, 4, 3, 5, 5, 6]
[0, 2, 3, 4, 3, 5, 5, 6]
6

"""