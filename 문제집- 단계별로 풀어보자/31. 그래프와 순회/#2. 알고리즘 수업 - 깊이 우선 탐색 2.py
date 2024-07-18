import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(N+1):
	graph[i].sort(reverse=True)


def dfs(v):
	global count
	count = count + 1
	visited[v] = count
	for nv in graph[v]:
		if visited[nv] == 0:
			dfs(nv)

visited = [0]*(N+1)
count = 0
dfs(R)

print(*visited[1:],sep='\n')