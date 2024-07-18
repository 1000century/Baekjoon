# 24.04.01 BFS

from collections import deque
import sys
input = sys.stdin.readline

def chess(I):
	stx,sty = map(int,input().split())
	enx,eny = map(int,input().split())

	q = deque([(stx,sty,0)])
	visited = set()
	visited.add((stx,sty))

	while q:
		nowx,nowy,cnt= q.popleft()
		if  nowx == enx and nowy==eny:
			print(cnt)
			break
		for nextx,nexty in [[nowx+1,nowy+2],[nowx+1,nowy-2],[nowx-1,nowy+2],[nowx-1,nowy-2]
					  		,[nowx+2,nowy+1],[nowx+2,nowy-1],[nowx-2,nowy+1],[nowx-2,nowy-1]]:
			if 0<=nextx <=I-1 and 0<=nexty <=I-1 and (nextx,nexty) not in visited:
				q.append((nextx,nexty,cnt+1))
				visited.add((nextx,nexty)) # 방문확인은 append 할 때 같이해야 함.
			
T = int(input())

for _ in range(T):
	i = int(input().rstrip())
	chess(i)

