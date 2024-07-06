import sys
sys.setrecursionlimit(1000000000)
rl = sys.stdin.readline
N = int(rl().rstrip())

graph =[[] for _ in range(N+1)]

for _ in range(N-1):
	a,b = map(int,rl().split())
	graph[a].append(b)
	graph[b].append(a)


def dfs(graph,visited,a=1):
	for next in graph[a]:
		if visited[next] == 0:
			visited[next] = a
			dfs(graph,visited,next)

visited = [0]*(N+1)
visited[1] = None
dfs(graph,visited)
print(*visited[2:],sep='\n')