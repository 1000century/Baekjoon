"""
DAG(directed acyclic graph)
위상정렬은 사이클이 발생하지 않는 방향 그래프에서 성립
"""
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())

ans = [0]* (N+1)
indegree = [0] * (N+1)
edges = [[] for _ in range(N+1)]
for _ in range(M):
	a,b = map(int,input().split())
	edges[a].append(b)
	indegree[b] = indegree[b] + 1

rank = deque([])


for i in range(1,N+1):
	if indegree[i] == 0:
		rank.append(i)
		ans[i] = 1

while rank:
	now = rank.popleft()
	for i in edges[now]:
		indegree[i] = indegree[i]-1
		if indegree[i] == 0:
			rank.append(i)
			ans[i] = ans[now]+1

for i in range(1,N+1):
	print(ans[i], end = " ")

