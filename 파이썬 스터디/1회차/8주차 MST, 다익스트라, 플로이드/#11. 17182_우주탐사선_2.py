"""
우주탐사선
https://www.acmicpc.net/problem/17182

>> 아이디어
플로이드 워셜 + 백트래킹(DFS)
"""

INF = int(1e9)

N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
	for a in range(N):
		for b in range(N):
			graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = INF
visited= [0]*(N)
visited[K] = 1

def dfs(s,d,depth):
	global ans
	if depth == N:
		ans = min(ans,d)
		return
	for i in range(N):
		if visited[i]:
			continue
		visited[i] = 1
		dfs(i,d+graph[s][i],depth+1)
		visited[i] = 0

dfs(K,0,1)
print(ans)
