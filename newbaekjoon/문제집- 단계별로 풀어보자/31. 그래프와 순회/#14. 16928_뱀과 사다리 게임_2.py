# 24.04.02
"""
시도 1) dp로 가다가 실패
시도 2) u랑 v를 반대로 적었다는 사실을 깨달음....
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
	shorcut[u] = v

q = deque([[1,0]])

while q:
	now,t = q.popleft()

	for next in [now+1,now+2,now+3,now+4,now+5,now+6]:
		if next > 100:
			continue

		if shorcut.get(next) == None: # 지름길이 없는 경우
			if t+1<visited[next]:
				visited[next] = t+1
				q.append([next,t+1])
		
		elif shorcut.get(next) != None:  # 지름길이 있는 경우
			if shorcut[next] == 100:visited[100] = min(visited[100],t+1)

			# 참고로 지름길이 있으면 100인 경우를 제외하고는 visited[next]는 업데이트 해주지 않음.
			if visited[shorcut[next]] > t+1:
				visited[shorcut[next]] = t+1
				q.append([shorcut[next],t+1])

print(visited[100])
