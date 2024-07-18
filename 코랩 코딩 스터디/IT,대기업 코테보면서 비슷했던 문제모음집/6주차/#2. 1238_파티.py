# (세현)

import heapq

INF = int(1e9)
N,M,X = map(int,input().split())

edges = {i:[] for i in range(1,N+1)}
edges_2 = {i:[] for i in range(1,N+1)}
for _ in range(M):
	s,e,t = map(int,input().split())
	edges[s] = edges[s]+[(e,t)]
	edges_2[e] = edges_2[e]+[(s,t)]

go = [INF]*(N+1)
go[X] = 0
q = []
heapq.heappush(q,(0,X))
while q:
	pd,pn = heapq.heappop(q)
	for nn,nd in edges[pn]:
		if go[nn] <= pd + nd:
			continue
		heapq.heappush(q,(pd+nd,nn))
		go[nn] = pd+nd

back = [INF]*(N+1)
back[X] = 0
q = []
heapq.heappush(q,(0,X))
while q:
	pd, pn = heapq.heappop(q)
	for nn,nd in edges_2[pn]:
		if back[nn] <= pd + nd:
			continue
		heapq.heappush(q,(pd+nd,nn))
		back[nn] = pd+nd

goback = [go[i]+back[i] for i in range(1,N+1)]
print(max(goback))