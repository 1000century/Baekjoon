from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(1,N+1):
	graph[i].sort(reverse=True)

visited = [0]*(N+1)
q = deque([R])
count = 1
visited[R] = count
while q:
	v = q.popleft()
	for nv in graph[v]:
		if visited[nv] == 0:
			q.append(nv)
			count = count + 1
			visited[nv] = count

print(*visited[1:],sep='\n')