"""
BFS를 함수가 아닌 while문을 이용해서 구현하였음
특히, queue를 이용해서 선입선출되는 개념 활용함
"""

from collections import deque

n = int(input())
A = list(map(int,input().split()))
s = int(input())

que = deque([s])

ans = set()
ans.add(s)
while que:
	new = que.pop()
	front = new + A[new-1]
	back = new - A[new-1]
	if front < n+1 and front not in ans:
		que.append(front)
		ans.add(front)
	if back >= 0+1 and back not in ans:
		que.append(back)
		ans.add(back)
print(len(ans))