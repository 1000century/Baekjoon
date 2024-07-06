"""
24.03.28
1) 이중탐색+BFS로 풀다가 실패
"""
import time
from collections import deque
N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

st = 1
en = 100

ans = 0
while st <= en:
	time.sleep(1)
	mid = (st + en) // 2
	count = 0
	visited = [[0]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if visited[j][i] == 0:
				visited[j][i] = 1
				if graph[j][i] > mid:
					count = count + 1

					q = deque([[i,j]])

					while q:
						x,y = q.pop()
						visited[y][x] = 1

						if y+1 <N and visited[y+1][x] ==0 and graph[y+1][x] > mid:
							q.append([x,y+1])
						if y-1 >=0 and visited[y-1][x] ==0 and graph[y-1][x] > mid:
							q.append([x,y-1])
						if x+1 <N and visited[y][x+1] ==0 and graph[y][x+1] > mid:
							q.append([x+1,y])
						if x-1 >=0 and visited[y][x-1] ==0 and graph[y][x-1] > mid:
							q.append([x-1,y])
	if count > ans:
		ans = count
		st = mid + 1

	else:
		en = mid - 1
	print("#########################",mid,ans)
print(ans)	
