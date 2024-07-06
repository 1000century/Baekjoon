"""
플로이드
https://www.acmicpc.net/problem/11404

전형적인 플로이드
"""
import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)
graph = [[INF]*(n) for _ in range(n)]

for _ in range(m):
	a,b,c= map(int,input().split())
	a,b = a-1,b-1
	graph[a][b] = min(graph[a][b],c)

for i in range(n):
	graph[i][i] = 0

for k in range(n):
	for a in range(n):
		for b in range(n):
			graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(n):
	for j in range(n):
		if graph[i][j] == INF:
			graph[i][j] = 0
for i in graph:
	print(*i)