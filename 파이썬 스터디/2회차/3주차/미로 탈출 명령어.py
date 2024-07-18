"""
미로 탈출 명령어
https://school.programmers.co.kr/learn/courses/30/lessons/150365
"""
from collections import deque
def solution(n, m, x, y, r, c, k):
	x,y,r,c = x-1,y-1,r-1,c-1
	if abs(r-x)+abs(c-y) > k:
		return 'impossible'
	
	cnt = k-abs(r-x)-abs(c-y)
	if cnt %2 == 1:
		return 'impossible'


	ans = []
	maze = [[int(1e9)]*m for _ in range(n)]
	q = deque([(x,y,'',0)])
	maze[x][y] = 0
	while q:
		px,py,pd,pk = q.popleft()
		for nx, ny,p in [(px+1,py,"d"),(px-1,py,'u'),(px,py+1,'r'),(px,py-1,'l')]:
			if not (0<=nx<n and 0<=ny<m):
				continue
			new = pd+p
			if (nx,ny) == (r,c) and pk+1==k:
				ans.append(new)
				continue
			if pk+1<k:
				q.append([nx,ny,new,pk+1])
	if len(ans) == 0:
		return "impossible"
	else:
		return sorted(ans)[0]
print(solution(3,4,2,3,3,1,5))