import sys
input = sys.stdin.readline
from collections import deque

a,b,c,d = map(int,input().split())
visited = set()
visited.add((0,0))
q = deque([[0,0,0]])
ans = -1

while q:
	x,y,cnt = q.popleft()
	if (x,y) == (c,d):
		ans = cnt
		break

	# part 1. fill and empty
	for nx,ny in [(a,y),(0,y),(x,b),(x,0)]:
		if (nx,ny) not in visited:
			visited.add((nx,ny))
			q.append([nx,ny,cnt+1])
	
	# part 2a) a to b
	if x+y >b:
		if (x+y-b,b) not in visited:
			visited.add((x+y-b,b))
			q.append([x-b+y,b,cnt+1])
	else:
		if (0,x+y) not in visited:
			visited.add((0,x+y))
			q.append([0,x+y,cnt+1])

	# part 2b) b to a
	if x+y > a:
		if (a,x+y-a) not in visited:
			visited.add((a,x+y-a))
			q.append([a,x+y-a,cnt+1])
	else:
		if (x+y,0) not in visited:
			visited.add((x+y,0))
			q.append([x+y,0,cnt+1])

print(ans)