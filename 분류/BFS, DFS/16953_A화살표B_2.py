"""
시도 1) dp + queue 메모리초과
시도 2) BFS
"""

from collections import deque
A,B = map(int,input().split())


q = deque([[A,1]])

while q:
	
	a,cnt = q.popleft()
	if a*2<int(B)+1:
		q.append([a*2,cnt+1])
		if a*2 == B:
			print(cnt+1)
			exit()
	if a*10+1 <int(B)+1:
		q.append([a*10+1,cnt+1])
		if a*10+1 == B:
			print(cnt+1)
			exit()
print(-1)