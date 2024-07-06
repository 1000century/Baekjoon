import sys
stick = list(sys.stdin.readline().rstrip())

count = 0
ans = 0
for i in range(len(stick)):
	if stick[i] == "(":
		if i +1 <= len(stick)-1 and stick[i+1] != ")":
			count = count + 1
	else:
		if i - 1 >0 and stick[i-1] != "(":
			ans = ans + 1
			count = count - 1
		else:
			ans = ans+ count

ans = ans + count
print(ans)

"""
import sys

stick = list(sys.stdin.readline().rstrip())

A = []
ans = 0
for i in range(len(stick)):
	if stick[i] == "(":
		if i +1 <= len(stick)-1 and stick[i+1] != ")":
			A.append(1)
	if stick[i] == ")":
		if i - 1 >0 and stick[i-1] != "(":
			ans = ans + A.pop()
		else:
			ans = ans+ len(A)

ans = ans + sum(A)
print(ans)
"""