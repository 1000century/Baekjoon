# 만약에 연결이 안되어있으면 어떻게 될까? >> 출발점이 1로 고정되어있으니까 INF롤 고정되어있을것

import heapq

N, M = map(int,input().split())

con =[[] for _ in range(N+1)]
for _ in range(M):
	a,b,c = map(int,input().split())
	con[a].append([b,c])
	con[b].append([a,c])

INF = int(1e9)
ways = [INF]*(N+1)
ways[1] = 0

q = []
heapq.heappush(q,(0,1))

while q:
	dist,node = heapq.heappop(q)
	if ways[node] < dist:
		continue
	for next,dd in con[node]:
		if dist + dd < ways[next]:
			ways[next] = dist + dd
			heapq.heappush(q,(dist+dd,next))
print(ways[N])