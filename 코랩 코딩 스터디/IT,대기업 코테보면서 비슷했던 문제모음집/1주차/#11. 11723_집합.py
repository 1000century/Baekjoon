# (세현)

import sys
input = sys.stdin.readline

M = int(input().rstrip())

S = set()
for _ in range(M):
	cmd = list(input().rstrip().split())
	if cmd[0] == "add":
		x = int(cmd[1])
		S.add(x)
	elif cmd[0] == "remove":
		x = int(cmd[1])
		S.discard(x)
	elif cmd[0] == "check":
		x = int(cmd[1])
		print(int(x in S))
	elif cmd[0] == "toggle":
		x = int(cmd[1])
		S ^={x}
	elif cmd[0] == "all":
		S = set([1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20])
	elif cmd[0] == "empty":
		S = set()
