"""
파티
https://www.acmicpc.net/problem/1238

"""
import heapq
N,M,X = map(int,input().split())
X = X-1
go = [[] for _ in range(N)]
back = [[] for _ in range(N)]
for _ in range(M):
	st, en, t = map(int,input().split())
	go[st-1] = go[st-1] +[(en-1,t)]
	back[en-1] = back[en-1] + [(st-1,t)]
INF = int(1e9)

dist = [INF]*N
dist[X] = 0
q = []
heapq.heappush(q,(0,X))
while q:
	d,p = heapq.heappop(q)
	if dist[p] < d: # 이거 없어도 통과됨
		continue
	for n,nd in go[p]:
		if nd+d<dist[n]:
			dist[n] = nd +d 
			heapq.heappush(q,(nd+d,n))

dist_back = [INF]*N
dist_back[X] = 0
q = []
heapq.heappush(q,(0,X))
while q:
	d,p = heapq.heappop(q)
	if dist_back[p] < d:
		continue
	for n,nd in back[p]:
		if nd +d <dist_back[n]:
			dist_back[n] = nd + d
			heapq.heappush(q,(nd+d,n))
ans = 0
for i in range(N):
	ans = max(ans,dist[i]+dist_back[i])
print(ans)
