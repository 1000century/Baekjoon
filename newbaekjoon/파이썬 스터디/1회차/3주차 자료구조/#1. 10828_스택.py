"""
함수 쓰니까 시간초과
"""
import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
	cmd = sys.stdin.readline().rstrip()

	if cmd == "top":
		if len(stack) !=0:
			print(stack[-1])
		else:
			print(-1)

	elif cmd == "pop":
		if not len(stack) == 0:
			print(stack.pop())
		else:
			print(-1)

	elif cmd == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)
			
	elif cmd == "size":
		print(len(stack))

	else:
		x = int(cmd[5:])
		stack.append(x)
