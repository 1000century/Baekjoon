# (세현)

import heapq
import sys

rl = sys.stdin.readline

V, E = map(int,rl().split()) # 정점개수, 간선개수
S = int(rl().rstrip()) # 출발점, 도착점

connection = [[] for _ in range(V+1)] # 다른 정점로 이동하는 방법
for _ in range(E):
	st, en, w = map(int,rl().split())
	connection[st].append([en,w])

INF = int(1e9)
dist_map = [INF]*(V+1) # 무한대로 초기화한 거리 지도
dist_map[S] = 0

q = [] # 저장용 heap
heapq.heappush(q,(0,S))
while q:
	dist,vertex = heapq.heappop(q)
	if dist_map[vertex] < dist:
		continue
	for next,price in connection[vertex]:
		new_dist = dist + price
		if new_dist < dist_map[next]:
			dist_map[next] = new_dist
			heapq.heappush(q,(new_dist,next))

for i in range(1,V+1):
	if dist_map[i] == INF:
		print("INF")
	else:
		print(dist_map[i])

