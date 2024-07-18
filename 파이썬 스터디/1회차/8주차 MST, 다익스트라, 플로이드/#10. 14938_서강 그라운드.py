"""
서강그라운드
https://www.acmicpc.net/problem/14938
"""

n,m,r = map(int,input().split())
t = list(map(int,input().split()))
INF = int(1e9)
graph = [[INF] *n for _ in range(n)]
for i in range(n):
	graph[i][i] = 0

for _ in range(r):
	a,b,l = map(int,input().split())
	a,b = a-1,b-1
	graph[a][b] = l
	graph[b][a] = l


for k in range(n):
	for a in range(n):
		for b in range(n):
			graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
#print(*graph,sep='\n')

ans = 0
for i in range(n):
	item = t[i]
	for j in range(n):
		if i != j:
			if graph[i][j]<=m:
				item = item + t[j]
	ans = max(ans,item)
print(ans)
