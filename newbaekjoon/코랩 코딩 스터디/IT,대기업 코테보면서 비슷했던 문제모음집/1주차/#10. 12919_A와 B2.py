# (세현)

from collections import deque

S = input()
T = input()

q = deque([])

q.append(T)
while q:
	x = q.popleft()
	if x == S:
		break
	if len(x) <=len(S):
		continue

	if x[-1] =="A":
		q.append(x[:-1])

	if x[0]== "B":
		q.append(x[1:][::-1])

print(int(x==S))