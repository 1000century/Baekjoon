# (세현)
"""
0-1 BFS sv djikstra
"""

import heapq

INF = int(1e9)
a,b = map(int,input().split())

dist = [INF]*100001

dist[a] = 0

q = []
heapq.heappush(q,(0,a))
while q:
	dist,now = heapq.heappop(q)
	if dist[now] < dist:
		continue
	if now-1>=0:
		next = now-1
		if dist[now]+1<dist[next]:
			dist[next] = dist[now] + 1
			heapq.heappush(q,(dist[now]+1,next))
	if now*2<=100000:
		next = now*2
		if dist[now]<dist[next]:
			dist[next] = dist[now]
			heapq.heappush(q,(dist[now],next))
	if now+1 <=100000:
		next = now+1
		if dist[now]+1<dist[next]:
			dist[next] = dist[now] +1
			heapq.heappush(q,(dist[now]+1,next))

print(dist[b])
	
