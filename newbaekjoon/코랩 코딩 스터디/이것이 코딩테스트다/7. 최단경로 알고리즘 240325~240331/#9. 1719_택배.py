# (세현)
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[[INF,0] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
	a,b,c = map(int,input().split())
	graph[a][b][0]= c
	graph[b][a][0]= c
	graph[a][b][1] = b
	graph[b][a][1] = a

for i in range(1,n+1):
	for j in range(1,n+1):
		if i == j:
			graph[i][j][0] = 0
			graph[i][j][1] = "-"

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			if graph[a][b][0] > graph[a][k][0] + graph[k][b][0]:
				graph[a][b][0] = graph[a][k][0]+graph[k][b][0]
				graph[a][b][1] = graph[a][k][1]  ## 갱신되는 시점에서 방문하는 도시랑 최단경로로 이동하기 위해 제일먼저 방문하는 도시랑 다르기 때문

"""

for i in range(1,n+1):
	for j in range(1,n+1):
		print(graph[i][j][0],end= " ")
	print()

print("위는 최단거리, 아래는 정답")

"""

for i in range(1,n+1):
	for j in range(1,n+1):
		print(graph[i][j][1],end= " ")
	print()


