"""
시도 1) deque > 실패
시도 2) heapq
"""

# (세현)

import sys
import heapq

rl = sys.stdin.readline
N, M, K, X = map(int,rl().split())

con = [[] for _ in range(N+1)]
distance = [int(1e9)]*(N+1)
distance[X] = 0

for _ in range(M):
	a,b = map(int,rl().split())
	con[a].append(b)

q = []
heapq.heappush(q,(0,X))
while q:
	d, node = heapq.heappop(q)
	if distance[node] < d:
		continue
	for eachNode in con[node]:
		temp = d + 1
		if temp < distance[eachNode]:
			distance[eachNode] = temp
			heapq.heappush(q,(temp,eachNode))
ans = []
for i in range(len(distance)):
	if distance[i] == K:
		ans.append(i)
if len(ans) == 0:
	print(-1)
else:
	print(*ans, sep='\n')

