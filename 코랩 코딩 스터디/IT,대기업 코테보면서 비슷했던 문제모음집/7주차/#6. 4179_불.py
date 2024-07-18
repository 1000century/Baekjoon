# (세현)
# 시간 3000ms >> bfs 하나로 통일해야 시간안에 통과할듯

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int,input().strip().split())

# Part 1. 미로 입력받기
firemaze = []
q = deque([])
ans = int(1e9)
for i in range(R):
	temp = list(list(input().strip()))
	second = [[i,int(1e9)] for i in temp]
	for j in range(len(temp)):
		if temp[j] == "F":
			fire= [i,j,0]
			q.append(fire)
			second[j][1]=0
	if "J" in temp:
		jihun = [i,temp.index("J"),0]
		if i ==0 or i == R-1 or temp.index("J") == 0 or temp.index("J")==C-1:
			ans = 1
	firemaze.append(second)
if ans == 1:
	print(1)
	exit()

# Part 2. 불이 붙는 시간 bfs
while q:
	r,c,t = q.popleft()
	for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
		if not (0<=nr<R and 0<=nc<C):
			continue
		if firemaze[nr][nc][0]=="#":
			continue
		if firemaze[nr][nc][1] > t+1:
			firemaze[nr][nc][1] = t+1
			q.append([nr,nc,t+1])

# Part 3. 지훈이가 있는 위치 bfs
q= deque([jihun])
visited = [[0]*C for _ in range(R)]
visited[jihun[0]][jihun[1]] = 1
while q:
	r,c,t = q.popleft()
	for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
		if not (0<=nr<R and 0<=nc<C):
			continue
		if firemaze[nr][nc][0]=="#":
			continue
		if visited[nr][nc] == 1:
			continue
		if firemaze[nr][nc][1]>t+1:
			if nr==0 or nr == R-1 or nc ==0 or nc == C-1:
				ans = min(ans,t+2)
			visited[nr][nc] = 1
			q.append([nr,nc,t+1])

# 정답
if ans == int(1e9):
	print("IMPOSSIBLE")
else:
	print(ans)