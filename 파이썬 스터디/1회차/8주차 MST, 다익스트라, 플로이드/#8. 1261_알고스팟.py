"""
알고스팟
https://www.acmicpc.net/problem/1261

2차원 데익스트라
"""
import heapq
import sys
input = sys.stdin.readline
M,N = map(int,input().split()) # M이 가로
graph = []
for _ in range(N):
	graph.append(list(map(int,input().replace(""," ").split())))

INF = int(1e9)
dist = [[INF]*(M) for _ in range(N)]
dist[0][0] = 0
q = []
heapq.heappush(q,(0,(0,0)))
while q:
	pd,(px,py) = heapq.heappop(q)
	if dist[px][py] < pd:
		continue
	for nx,ny in [(px+1,py),(px-1,py),(px,py+1),(px,py-1)]:
		if not (0<=nx<N and 0<=ny<M):
			continue
		if graph[nx][ny] ==0:
			if pd < dist[nx][ny]:
				dist[nx][ny] = pd
				heapq.heappush(q,(pd,(nx,ny)))
		else:
			if pd + 1 <dist[nx][ny]:
				dist[nx][ny] = pd+1
				heapq.heappush(q,(pd+1,(nx,ny)))

print(dist[-1][-1])