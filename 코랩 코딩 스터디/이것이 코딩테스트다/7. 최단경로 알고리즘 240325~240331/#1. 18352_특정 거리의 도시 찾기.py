"""
실패
"""

from collections import deque

N, M, K, X = map(int,input().split())

dist = [[0]*(M+1) for _ in range(N+1)]

for _ in range(M):
	a,b = map(int,input().split())
	dist[b][a] = 1

print(dist)

count = [[0]*(N+1) for _ in range(N+1)]

def bfs(dist,a,b):
	queue = deque([[a,b]])
	count[b][a] += 1  ## 방문함수 on
	while queue:
		x, y = queue.popleft()
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x + dx, y + dy
			# nx, ny가 범위 내에 있고 방문가능하지만 방문하지 않았을 떄
			if 0 < nx < len(dist[0]) and 0 < ny < len(dist) and dist[ny][nx] and count[ny][nx] == 0:
				count[ny][nx] = count[y][x] + dist[y][x]
				queue.append([nx, ny])
	#print("QUEUE")
	#print(queue)
	#print("COUNT")
	#print(*count, sep='\n')

	print(*count, sep='\n')

bfs(dist,1,1)