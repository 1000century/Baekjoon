"""
24.03.12 00:09~
pop 하면 33%에서 시간초과 생김
왜인지는 모름
"""
import math
import sys
n = int(sys.stdin.readline())
diff = []
for _ in range(n):
	new = int(sys.stdin.readline())
	if new ==0:
		n = n-1
	else:
		diff.append(int(new))
		
diff.sort()

x = n*0.15 +0.5
p = math.floor(x)
p = int(p)
n = n-2* p

if n == 0:
	print(0)
else:
	if p != 0:
		print(math.floor(0.5+sum(diff[p:-p])/n))
	else:
		print(math.floor(0.5+sum(diff)/n))
