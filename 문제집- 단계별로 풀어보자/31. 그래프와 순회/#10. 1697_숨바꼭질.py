# 24.04.01 BFS

from collections import deque
N, K = map(int,input().split())

q = deque([(N,0)])
visited = set()
visited.add(N)

while q:
	now,time = q.popleft()
	if now == K:
		print(time)
		break
	for next in [now+1,now-1,now*2]:
		if 0<=next <=100000 and next not in visited:
			q.append((next,time+1))
			visited.add(next) # 방문확인은 append 할 때 같이해야 함.
			
