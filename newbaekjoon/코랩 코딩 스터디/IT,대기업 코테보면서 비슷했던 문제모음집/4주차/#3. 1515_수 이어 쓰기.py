"""
https://www.acmicpc.net/problem/1515
"""
# (세현)

goal = input()
ans = 1
string = str(1)
while True:
	while string and goal:
		a,b = string[0], goal[0]
		if a == b:
			goal = goal[1:]
		string = string[1:]

	if not goal:
		print(ans)
		exit()

	ans = ans + 1
	string = string + str(ans)