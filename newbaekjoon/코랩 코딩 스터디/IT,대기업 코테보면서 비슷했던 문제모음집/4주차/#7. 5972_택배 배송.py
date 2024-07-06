# (세현)

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
dist = [INF]*(N+1)
dist[1] = 0

for _ in range(M):
	st, en, c = map(int,input().split())
	graph[st].append((en,c))
	graph[en].append((st,c))

q = []
heapq.heappush(q,[0,1])

while q:
	d,current_node = heapq.heappop(q)
	for next_node,next_cost in graph[current_node]:
		if d + next_cost < dist[next_node]:
			dist[next_node] = d + next_cost
			heapq.heappush(q,[d+next_cost,next_node])
print(dist[-1])