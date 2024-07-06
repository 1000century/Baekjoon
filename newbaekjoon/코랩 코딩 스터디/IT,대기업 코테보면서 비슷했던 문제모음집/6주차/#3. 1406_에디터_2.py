import sys
input = sys.stdin.readline
from collections import deque

front = deque(list(input().rstrip().replace(""," ").split()))
back = deque([])

M = int(input())
for i in range(M):
	cmd = input().rstrip()
	if cmd[0] == "L":
		if front:
			back.appendleft(front.pop())
	elif cmd[0] == "D":
		if back:
			front.append(back.popleft())
	elif cmd[0] == "B":
		if front:
			front.pop()
	else:
		x = cmd[-1]
		front.append(x)
print(''.join(front+back))