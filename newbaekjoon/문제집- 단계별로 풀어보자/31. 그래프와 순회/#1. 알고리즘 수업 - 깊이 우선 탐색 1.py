import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(1,N+1):
	graph[i].sort()

visited = [0]*(N+1)

count = 0
def dfs(n):
	global count
	count = count + 1
	visited[n] = count
	for next in graph[n]:
		if visited[next] == 0:
			dfs(next)

dfs(R)
print(*visited[1:],sep='\n')