# (세현)

""" 뭔가 더 빨리 푸는 게 있을 듯 """

import heapq

N,M,X = map(int,input().split())

road = [[] for _ in range(N+1)]
r_road = [[] for _ in range(N+1)]
for _ in range(M):
	s,e,t = map(int,input().split())
	road[s].append((e,t))
	r_road[e].append((s,t))

INF = int(1e9)
dist = [INF]*(N+1)
r_dist = [INF]*(N+1)

q = []
r_q = []

dist[X] = 0
r_dist[X] = 0

heapq.heappush(q,(0,X))
heapq.heappush(r_q,(0,X))

while q:
	cnt_d, cnt_n = heapq.heappop(q)
	if dist[cnt_n] < cnt_d:
		continue
	for e,t in road[cnt_n]:
		if cnt_d + t < dist[e]:
			dist[e] = cnt_d + t
			heapq.heappush(q,(cnt_d+t,e))

while r_q:
	cnt_d, cnt_n = heapq.heappop(r_q)
	if r_dist[cnt_n] < cnt_d:
		continue
	for e,t in r_road[cnt_n]:
		if cnt_d + t < r_dist[e]:
			r_dist[e] = cnt_d + t
			heapq.heappush(r_q,(cnt_d+t,e))

#print(dist)	[1000000000, 1, 0, 3, 7]
#print(r_dist)	[1000000000, 4, 0, 6, 3]

ans = 0
for i in range(1,N+1):
	ans = max(ans,dist[i]+r_dist[i])
print(ans)
