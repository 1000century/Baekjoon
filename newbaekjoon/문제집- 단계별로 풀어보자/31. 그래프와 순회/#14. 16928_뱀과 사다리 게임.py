# 24.04.02
"""
시도 1) dp로 가다가 실패
"""

from collections import deque

N,M = map(int,input().split())

INF = int(1e9)
visited = [INF]*101
visited[0] = -1
visited[1] = 0

shorcut = {}

for _ in range(N): # 사다리
	x,y = map(int,input().split())
	shorcut[x] = y

for _ in range(M): # 뱀의 정보
	u,v = map(int,input().split())
	shorcut[v] = u

q = deque([[1,0]])

while q:
	now,t = q.popleft()

	for next in [now+1,now+2,now+3,now+4,now+5,now+6]:
		if next > 100:
			continue

		if visited[next] > t+1:
			visited[next] = min(visited[next],t+1)
			q.append([next,visited[next]])

		if shorcut.get(next) != None and visited[shorcut[next]] > visited[next]:
			visited[shorcut[next]] = visited[next]
			q.append([shorcut[next],visited[next]]) # 최종 것을 append
print()
print(visited)

