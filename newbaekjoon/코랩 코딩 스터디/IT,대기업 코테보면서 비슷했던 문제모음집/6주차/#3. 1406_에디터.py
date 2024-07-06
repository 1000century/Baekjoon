import sys
input = sys.stdin.readline

char = list(input().rstrip().replace(""," ").split())

M = int(input())
cursor = len(char)
for i in range(M):
	cmd = input().rstrip()
	if cmd[0] == "L":
		cursor = max(0,cursor -1)
	elif cmd[0] == "D":
		cursor = min(len(char),cursor+1)
	elif cmd[0] == "B":
		if cursor == 0:
			continue
		del char[cursor-1]
		cursor = cursor-1

	else:
		x = cmd[-1]
		char.insert(cursor,x)
		cursor = cursor + 1
print(*char,sep='')

