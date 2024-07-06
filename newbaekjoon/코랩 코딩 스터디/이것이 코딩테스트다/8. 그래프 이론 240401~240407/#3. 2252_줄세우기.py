"""
DAG(directed acyclic graph)
위상정렬은 사이클이 발생하지 않는 방향 그래프에서 성립
"""
# (세현)

from collections import deque
N, M = map(int,input().split())

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

while rank:
	now = rank.popleft()
	print(now,end=" ")
	for i in edges[now]:
		indegree[i] = indegree[i]-1
		if indegree[i] == 0:
			rank.append(i)

