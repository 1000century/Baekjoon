"""
특정한 최단경로
https://www.acmicpc.net/problem/1504

표준입력 안쓰면 시간초과 생김.

"""
import sys
import heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
	a,b,c = map(int,input().split())
	graph[a].append((b,c))
	graph[b].append((a,c))
v1,v2 = map(int,input().split())
INF = int(1e9)

# 1에서 시작하는 다익스트라
dist = [INF]*(N+1)
dist[1] = 0
q = []
heapq.heappush(q,(0,1))
while q:
	pd,pn = heapq.heappop(q)
	if dist[pn] < pd:
		continue
	for nn,nd in graph[pn]:
		if nd + pd <dist[nn]:
			dist[nn] = nd+pd
			heapq.heappush(q,(nd+pd,nn))

# v1에서 시작하는 다익스트라
dist_v1 = [INF]*(N+1)
dist_v1[v1] = 0
q = []
heapq.heappush(q,(0,v1))
while q:
	pd,pn = heapq.heappop(q)
	if dist_v1[pn] < pd:
		continue
	for nn,nd in graph[pn]:
		if nd + pd <dist_v1[nn]:
			dist_v1[nn] = nd+pd
			heapq.heappush(q,(nd+pd,nn))

# v2에서 시작하는 다익스트라
dist_v2 = [INF]*(N+1)
dist_v2[v2] = 0
q = []
heapq.heappush(q,(0,v2))
while q:
	pd,pn = heapq.heappop(q)
	if dist_v2[pn] < pd:
		continue
	for nn,nd in graph[pn]:
		if nd + pd <dist_v2[nn]:
			dist_v2[nn] = nd+pd
			heapq.heappush(q,(nd+pd,nn))


# 최종 정답하는 코드
path1 = INF
path2 = INF
if  dist[v1]!= INF and dist_v2[-1] != INF:
	path1=dist[v1] + dist_v1[v2] + dist_v2[-1]
if dist[v2] != INF and dist_v1[-1] != INF:	
	path2 = dist[v2] + dist_v2[v1] + dist_v1[-1]

path = min(path1,path2)
if path == INF:
	print(-1)
else:
	print(path)
