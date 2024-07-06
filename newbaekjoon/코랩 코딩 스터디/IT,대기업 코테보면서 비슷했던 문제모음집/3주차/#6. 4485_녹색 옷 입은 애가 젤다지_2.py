# (세현)

# 시도 1) bfs로 하니까 시간초과
# 시도 2) 다익스트라

import heapq
INF = int(1e9)
def zelda(N,count):
	lupi = [list(map(int,input().split())) for _ in range(N)]
	dp = [[INF]*N for _ in range(N)]
	dp[0][0] = lupi[0][0]
	q = []
	heapq.heappush(q,(lupi[0][0],0,0))

	while q:
		l,x,y = heapq.heappop(q)
		for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if not (0<=nx< N and 0<=ny<N):
				continue
			if l+lupi[nx][ny] < dp[nx][ny]:
				dp[nx][ny] = l+lupi[nx][ny]
				heapq.heappush(q,(dp[nx][ny],nx,ny))
	print(f"Problem {count}: {dp[-1][-1]}")

count = 0
while True:
	count = count + 1
	N = int(input())
	if N == 0:
		break
	zelda(N,count)