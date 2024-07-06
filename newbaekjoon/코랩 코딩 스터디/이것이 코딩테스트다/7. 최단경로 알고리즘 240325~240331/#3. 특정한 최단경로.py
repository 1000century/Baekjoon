# (세현)
"""
https://www.acmicpc.net/problem/1504
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N,E = map(int,input().split())

con = [[] for _ in range(N+1)]
for _ in range(E):
	a,b,dd = map(int,input().split())
	con[a].append([b,dd])
	con[b].append([a,dd])

v1,v2 = map(int,input().split())


def djikstra(N,st):
	visited = [INF]*(N+1)
	visited[st] = 0
	q = []
	heapq.heappush(q,(0,st))
	while q:
		dist,now = heapq.heappop(q)
		if visited[now] < dist:
			continue
		for next,dd in con[now]:
			if dist+dd < visited[next]:
				visited[next] = dd + dist
				heapq.heappush(q,(dd + dist,next))
	return(visited)


dj1 = djikstra(N,1)
djv1 = djikstra(N,v1)
djv2 = djikstra(N,v2)

a = dj1[v1] + djv1[v2] + djv2[N]
b = dj1[v2] + djv2[v1] + djv1[N]

if min(a,b) >= INF:
	print(-1)
else:
	print(min(a,b))