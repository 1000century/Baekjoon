# 시도 1) cost[next] = cost[now] + time[next] 해서 틀림

from collections import deque

N = int(input())

time = [0]*(N+1)
indegree =[0]*(N+1)
graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
	a = list(map(int,input().split()))
	time[i] = int(a[0])
	if a[1] !=0:
		for before in a[2:]:
			graph[before].append(i)
			indegree[i] = indegree[i] + 1

cost = [0]*(N+1)
q = deque([])
for i in range(1,N+1):
	if indegree[i] ==0:
		q.append(i)
		cost[i] = time[i]

while q:
	now = q.popleft()
	for next in graph[now]:
		indegree[next] = indegree[next] - 1
		cost[next] = max(cost[next],cost[now] + time[next])
		if indegree[next] == 0:
			q.append(next)
print(max(cost))