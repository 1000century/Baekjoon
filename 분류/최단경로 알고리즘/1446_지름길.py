import heapq
N,D = map(int,input().split())

con = [[(i+1,1)] for i in range(10000)]+[()]

for _ in range(N):
	st, en, d = map(int,input().split())
	con[st].append((en,d))

INF = int(1e9)
ways = [INF]*10001
ways[0] = 0

q = []
heapq.heappush(q,(0,0))
while q:
	dist, node = heapq.heappop(q)
	if ways[node] < dist:
		continue
	for next,dd in con[node]:
		if  dist + dd < ways[next]:
			ways[next] = dist + dd
			heapq.heappush(q,(dist+dd,next))

print(ways[D])