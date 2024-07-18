# 3차원 BFS

from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int,input().split())
jido = [list(input()) for i in range(N)]

# dist[x][y][0]: 벽을 부수지 않고 (x, y)까지 도달하는 최소 거리
# dist[x][y][1]: 벽을 부수고 (x, y)까지 도달하는 최소 거리
dist = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]

# BFS 초기 설정: (x 좌표, y 좌표, 벽 부순 여부)
queue = deque([(0, 0, 0)])
dist[0][0][0] = 1

# 이동 가능한 방향 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
	x, y, broke = queue.popleft()
	
	for dx, dy in directions:
		nx, ny = x + dx, y + dy
		if 0 <= nx < N and 0 <= ny < M:
			if jido[nx][ny] == '0' and dist[nx][ny][broke] == float('inf'):
				# 벽이 아니고 아직 방문하지 않은 경우
				dist[nx][ny][broke] = dist[x][y][broke] + 1
				queue.append((nx, ny, broke))
			elif jido[nx][ny] == '1' and broke == 0:
				# 벽이고 벽을 부순 적이 없는 경우
				dist[nx][ny][1] = dist[x][y][broke] + 1
				queue.append((nx, ny, 1))

answer = min(dist[N-1][M-1])
if answer == float('inf'):
	print(-1)
else:
	print(answer)
