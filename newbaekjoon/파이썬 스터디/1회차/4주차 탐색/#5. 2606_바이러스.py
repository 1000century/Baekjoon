"""
24.03.28
bfs보다는 dfs가 더 빠른 거 같음
"""

from collections import deque

N = int(input())

computers = [[] for _ in range(N+1)]
E = int(input())
for _ in range(E):
	a,b = map(int,input().split())
	computers[a].append(b)
	computers[b].append(a)

for i in range(1,N+1):
	computers[i] = sorted(computers[i])


def bfs(computers):
	visited = [0]*(N+1)
	q = deque([1])
	count = 0
	while q:
		a = q.popleft()
		visited[a] = 1
		count = count + 1
		for i in computers[a]:
			if visited[i] == 0:
				q.append(i)
				visited[i] = 1
	#print(*computers, end ='\n')
	print(count-1)
	#print(visited)

bfs(computers)