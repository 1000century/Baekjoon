from collections import deque

N,M = map(int,input().split())

graph= [[0]*(M+1) for _ in range(N+1)]
count= [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
	graph[i] = [0]+list(map(int,input().replace(" ", "")))
#print(*graph, sep='\n')

def bfs(graph,a,b):
	queue = deque([[a,b]])
	count[b][a] += 1  ## 방문함수 on
	while queue:
		x, y = queue.popleft()
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x + dx, y + dy
			# nx, ny가 범위 내에 있고 방문가능하지만 방문하지 않았을 떄
			if 0 < nx < len(graph[0]) and 0 < ny < len(graph) and graph[ny][nx] and count[ny][nx] == 0:
				count[ny][nx] = count[y][x] + 1
				queue.append([nx, ny])
	#print("QUEUE")
	#print(queue)
	#print("COUNT")
	#print(*count, sep='\n')

	print(count[-1][-1])
bfs(graph,1,1)