"""
시도 1) 메모리초과
"""

from collections import deque
A,B = map(int,input().split())

dp = [int(1e9)]*(B+1)

dp[A]  = 0

q = deque([A])

while q:
	a = q.popleft()
	if a*2<int(B)+1:
		dp[a*2] = min(dp[a*2],dp[a] + 1)
		q.append(a*2)
	if a*10+1 <int(B)+1:
		dp[a*10+1] = min(dp[a*10+1],dp[a] + 1)
		q.append(a*10+1)
if dp[B] == int(1e9):
	print(-1)
else:
	print(dp[B]+1)