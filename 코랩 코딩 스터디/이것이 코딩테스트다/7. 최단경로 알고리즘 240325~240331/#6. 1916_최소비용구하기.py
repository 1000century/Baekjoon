# (세현)

import heapq
import sys

rl = sys.stdin.readline

N = int(rl().rstrip()) # 도시
M = int(rl().rstrip()) # 버스

city_connect = [[] for _ in range(N+1)] # 다른 도시로 이동하는 방법
for _ in range(M):
	st, en, p = map(int,rl().split())
	city_connect[st].append([en,p])

S, E = map(int,rl().split()) # 출발도시, 도착도시

INF = int(1e9)
dist_map = [INF]*(N+1) # 무한대로 초기화한 거리 지도
dist_map[S] = 0

q = [] # 저장해두는 heap
heapq.heappush(q,(0,S))
while q:
	dist,city = heapq.heappop(q)
	if dist_map[city] < dist:
		continue
	for next,price in city_connect[city]:
		new_dist = dist + price
		if new_dist < dist_map[next]:
			dist_map[next] = new_dist
			heapq.heappush(q,(new_dist,next))
print(dist_map[E])

