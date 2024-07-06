import sys
input = sys.stdin.readline

# Part 1. 준비
N = int(input().rstrip())
M = int(input().rstrip())

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
	a,b,c = map(int,input().split())
	graph[a][b] = min(graph[a][b],c)

for i in range(1,N+1):
	graph[i][i] = 0

# Part 2. 플로이드 워셜
for k in range(1,N+1):
	for a in range(1,N+1):
		if a == k:
			continue
		for b in range(1,N+1):
			graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# Part 3. 출력
for i in range(1,N+1):
	for j in range(1,N+1):
		if graph[i][j] != INF:
			print(graph[i][j],end=" ")
		else:
			print(0,end=" ")
	print()