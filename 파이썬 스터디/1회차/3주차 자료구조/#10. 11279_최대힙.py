"""
124ms
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = []
for _ in range(N):
	x = int(input().rstrip())
	
	if not x == 0:
		heapq.heappush(A,-x)
	else:
		if len(A) == 0:
			print(0)
#			print("ans",0)
		else:
			print(-heapq.heappop(A))
#			print("ans",-heapq.heappop(A))

