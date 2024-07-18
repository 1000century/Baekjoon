# 24.04.01 BFS

# 시작점이 여러개인 BFS 문제 >> 모든 시작점으 큐에 넣고 bfs를 돌림

import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

q = deque([])
visited = set()


for i in range(N): # N,i은 세로
	for j in range(M): # M,j은 가로
		if graph[i][j] == 1:
			q.append((i,j,0))
			visited.add((i,j))
			ans = 0
		if graph[i][j] == -1:
			visited.add((i,j))
ans = -1
while q:
	a,b,t = q.popleft()
	for na,nb in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
		if 0<=na<N and 0<=nb<M and (na,nb) not in visited:
			visited.add((na,nb))
			q.append((na,nb,t+1))
	ans = max(ans,t)

if len(visited) == M*N:
	print(ans)
else:
	print(-1)
