# (세현)

import heapq

M,N = map(int,input().split())
X = [list(map(int,input().replace(""," ").split())) for _ in range(N)]

INF = int(1e9)
dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0

q = []
heapq.heappush(q,(0,(0,0)))

while q:
	d,(a,b) = heapq.heappop(q)
	if dist[a][b] < d:
		continue
	for y,x in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
		if 0<=x<M and 0<=y<N:
			if X[y][x] == 1:		 # 막혀있을 때
				if d + 1 < dist[y][x]:
					dist[y][x] = d + 1
					heapq.heappush(q,(d+1,(y,x)))
			else:			 		 # 뚫려있을 때
				if d < dist[y][x]:
					dist[y][x] = d
					heapq.heappush(q,(d,(y,x)))

#print(*dist, sep= '\n')
print(dist[N-1][M-1])