# 24.04.02
from collections import deque

N,M = map(int,input().split())

graph = [list(map(int,input().replace(""," ").split())) for _ in range(N)]


q = deque([])
q.append([0,0,0])
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
ans = [[0]*M for _ in range(N)]
while q:
	x,y,t = q.popleft()
	for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
		nx = x + dx
		ny = y + dy
		if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
			visited[nx][ny] = 1
			if graph[nx][ny] == 1:
				if graph[nx+dx][ny+dy] == 0 and 0<=nx+dx<N and 0<=ny+dy<M and visited[nx+dx][ny+dy] == 0:
					q.append([nx+dx,ny+dy,t+1])
					ans[nx+dx][ny+dy] = t+1
			elif graph[nx][ny] == 0:
				q.append([nx,ny,t+1])
				ans[nx][ny] = t+1
print(ans)

