"""
24.03.28
방문 처리는 q에 넣을 때 해야함. q에서 뺄때 하면 시간초과나옴
"""

import sys
rl = sys.stdin.readline

from collections import deque

N,M = map(int,rl().split())

connect = [[] for _ in range(N+1)]

for _ in range(M):
	a,b = map(int,rl().split())
	connect[a].append(b)
	connect[b].append(a)
for i in range(1,N+1):
	connect[i] = sorted(connect[i])

def dfs(N,connect):
	count = 0
	visited = set()
	for i in range(1,N+1):
		if i in visited:
			continue
		count = count + 1
		q = deque([i])
		visited.add(i)
		while q:
			now = q.popleft()
			for next in connect[now]:
				if next not in visited:
					q.append(next)
					visited.add(next)
					
	print(count)
dfs(N,connect)
