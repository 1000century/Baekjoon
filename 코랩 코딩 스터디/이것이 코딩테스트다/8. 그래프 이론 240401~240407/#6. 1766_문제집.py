# (세현)

import heapq
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
	a,b = map(int,input().split())
	graph[a].append(b)
	indegree[b] = indegree[b] + 1
#print(graph)
#print(indegree)

X = []
for i in range(1,N+1):
	if indegree[i] ==0:
		heapq.heappush(X,i)

while X:
	now = heapq.heappop(X)
	print(now,end=" ")
	for i in graph[now]:
		indegree[i] = indegree[i]-1
		if indegree[i] == 0:
			heapq.heappush(X,i)
