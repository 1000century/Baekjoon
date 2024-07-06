import math
N = int(input())

k = ((8*N+1)**0.5-1)/2
k = math.ceil(k)
print(k)
from collections import deque
rt = deque([])
lt = deque([])
for i in range(1,k+1):
	if i%2 == 1:
		rt.append(i)
	else:
		lt.appendleft(i)
print(*rt, *lt)