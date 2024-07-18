from collections import deque
def bfs(p):
	start = []
	
	for i in range(5):
		for j in range(5):
			if p[i][j] == 'P':
				start.append([i, j])
	
	for s in start:
		queue = deque([s])
		visited = [[0]*5 for i in range(5)]
		distance = [[0]*5 for i in range(5)]
		visited[s[0]][s[1]] = 1
		
		while queue:
			y, x = queue.popleft()

			for nx,ny in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
				if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
					
					if p[ny][nx] == 'O':
						queue.append([ny, nx])
						visited[ny][nx] = 1
						distance[ny][nx] = distance[y][x] + 1
					
					if p[ny][nx] == 'P' and distance[y][x] <= 1:
						return 0
	return 1

def solution(places):
	answer = []
	for i in places:
		answer.append(bfs(i))	
	return answer