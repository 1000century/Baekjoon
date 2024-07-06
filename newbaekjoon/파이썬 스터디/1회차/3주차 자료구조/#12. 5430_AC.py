"""
152ms
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = []
for _ in range(N):
	x = int(input().rstrip())
	
	if not x == 0:
		heapq.heappush(A,(abs(x),x))
	else:
		if len(A) == 0:
			print(0)
#			print("ans",0)
		else:
			print(heapq.heappop(A)[1])
#			print("ans",heapq.heappop(A)[1])

