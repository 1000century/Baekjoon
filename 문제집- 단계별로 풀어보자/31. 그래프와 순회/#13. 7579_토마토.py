# 24.04.01 BFS

# 시작점이 여러개인 BFS 문제 >> 모든 시작점으 큐에 넣고 bfs를 돌림

import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())

graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

q = deque([])
visited = set()

for h in range(H):
	for i in range(N): # N,i은 세로
		for j in range(M): # M,j은 가로
			if graph[h][i][j] == 1:
				q.append((h,i,j,0))
				visited.add((h,i,j))
				ans = 0
			if graph[h][i][j] == -1:
				visited.add((h,i,j))
ans = -1
while q:
	c,a,b,t = q.popleft()
	for nc,na,nb in [(c+1,a,b),(c-1,a,b),
					(c,a+1,b),(c,a-1,b),
				  	(c,a,b+1),(c,a,b-1)]:
		if 0<=nc<H and 0<=na<N and 0<=nb<M and (nc, na,nb) not in visited:
			visited.add((nc,na,nb))
			q.append((nc,na,nb,t+1))
	ans = max(ans,t)

if len(visited) == H*M*N:
	print(ans)
else:
	print(-1)
