# (세현)

N = int(input())

graph = []

for i in range(N):
	graph.append(list(map(int,input().split())))
#print(*graph, sep="\n")

for k in range(N):
	for a in range(N):
		for b in range(N):
			if graph[a][b] ==0 and graph[a][k] and graph[k][b]:
				graph[a][b] = 1

for line in graph:
	print(*line)
