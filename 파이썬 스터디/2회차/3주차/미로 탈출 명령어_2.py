"""
미로 탈출 명령어
https://school.programmers.co.kr/learn/courses/30/lessons/150365
"""
from collections import deque
def solution(n, m, x, y, r, c, k):
	if (k-abs(r-x)-abs(c-y))%2 == 1:
		return "impossible"
	
	rest = k-abs(r-x)-abs(c-y)

	ud,rl = [],[]
	if r>x:		ud = ['d']*(r-x)
	elif x>r:	ud = ['u']*(x-r)
	if c>y:		rl = ['l']*(c-y)
	elif c<y:	rl = ['r']*(y-c)

	
	while rest != 0:
		if 	

	
	rest = k-abs(r-x)-abs(c-y)


	return
print(solution(3,4,2,3,3,1,5))