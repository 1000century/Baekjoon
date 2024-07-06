# (세현)
# 아이디어 : target에서 시작해서 도달가능한 곳만 거리 업데이트

from collections import deque

n,m = map(int,input().split())
maps = []
distance = [[-1]*m for _ in range(n)] # 모든 거리를 -1로 초기화

for i in range(n):
	temp = list(map(int,input().split()))
	maps.append(temp)
	for j in range(m):
		if temp[j] ==0: # 애초에 도달불가능한 경우 >> 0으로 표현
			distance[i][j] = 0
		elif temp[j] == 2: # target인 경우 >> 0으로 표현
			distance[i][j] = 0
			q = deque([[i,j,0]]) # target만 deque으로 추가

while q:
	x,y,d = q.popleft()
	for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
		if not (0<=nx<n and 0<=ny<m): # nx,ny 범위제한 확인
			continue
		if distance[nx][ny] != -1: # 방문여부 확인
			continue

		if maps[nx][ny] == 1:
			q.append([nx,ny,d+1])
			distance[nx][ny] = d+1
		 	##	bfs방식이므로 최솟값 비교해주지 않아도 됨
				
for i in range(n):
	print(*distance[i])