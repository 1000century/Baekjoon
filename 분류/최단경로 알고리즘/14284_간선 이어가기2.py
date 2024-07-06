# 시도 1) 처음에 무방향 그래프인 거 생각하지 몼하고 graph[a] 만 append했음
# 시도 2) graph[b] 추가하니까 맞았음.

import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
	a,b,c = map(int,input().split())
	graph[a].append([b,c])
	graph[b].append([a,c])

s,t = map(int,input().split())

INF = int(1e9)
ways = [INF] * (n+1)
ways[s] = 0

q = []
heapq.heappush(q,(0,s))

while q:
	cost, v = heapq.heappop(q)
	if cost > ways[v]:
		continue
	for nv,nc in graph[v]:
		temp = nc + cost
		if temp < ways[nv]:
			ways[nv] = temp
			heapq.heappush(q,(temp,nv))

print(ways[t])