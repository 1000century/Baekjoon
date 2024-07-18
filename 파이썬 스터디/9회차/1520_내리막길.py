import sys
input = sys.stdin.readline

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

import heapq
q = []

heapq.heappush(q,[arr[0][0],0,0])
cost = [[0]*N for _ in range(M)]
cost[0][0] = 1

while q:
	x,m,n = heapq.heappop(q)
	if m == M and n == N:
		continue
	for mm, nn in [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]:
		if not (0<=mm<M and 0<=nn<N):
			continue
		if arr[mm][nn]>= arr[m][n]:
			continue
		if cost[mm][nn] == 0:
			heapq.heappush(q,[-arr[mm][nn],mm,nn])
		cost[mm][nn] = cost[m][n] + cost[mm][nn]

print(cost[-1][-1])