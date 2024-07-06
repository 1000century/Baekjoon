from collections import deque
INF = int(1e9)
def solution(n, s, a, b, fares):
	graph = [[INF]*(n+1) for _ in range(n+1)]
	for x,y,c in fares:
		graph[x][y] = c
		graph[y][x] =c
	
	for i in range(0,n+1):
		graph[i][i] = 0

	for k in range(0,n+1):
		for x in range(0,n+1):
			for y in range(0,n+1):
				graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])
	answer = INF
	for i in range(1,n+1):
		answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

	return answer
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

