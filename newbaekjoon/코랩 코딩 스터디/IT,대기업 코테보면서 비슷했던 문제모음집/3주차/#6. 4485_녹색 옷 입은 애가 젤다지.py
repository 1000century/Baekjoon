# 시도 1) bfs로 하니까 시간초가

import sys
input = sys.stdin.readline
from collections import deque

def zelda(N,count):
	lupi = [list(map(int,input().split())) for _ in range(N)]
	dp = [[-1]*N for _ in range(N)]
	dp[0][0] = lupi[0][0]
	q = deque([[0,0,lupi[0][0]]])

	while q:
		x,y,l = q.popleft()
		for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if not (0<=nx< N and 0<=ny<N):
				continue
			if dp[nx][ny] == -1:
				dp[nx][ny] = l+lupi[nx][ny]
				q.append([nx,ny,dp[nx][ny]])
			else:
				if l+lupi[nx][ny] < dp[nx][ny]:
					dp[nx][ny] = l+lupi[nx][ny]
					q.append([nx,ny,l+lupi[nx][ny]])
	print(f"Problem {count}: {dp[-1][-1]}")





count = 0
while True:
	count = count + 1
	N = int(input())
	if N == 0:
		break
	zelda(N,count)