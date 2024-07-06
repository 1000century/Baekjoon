"""
24.03.28
시도 1) 처음엔 bfs로 풀어도 될 줄 알았는데 안풀림
"""

from collections import deque

n = int(input())
x,y = map(int,input().split())
A = [[] for _ in range(n+1)]
e = int(input())
for _ in range(e):
	a,b = map(int,input().split())
	A[a].append(b)
	A[b].append(a)
for i in range(1,n+1):
	A[i] = sorted(A[i])

visited = [0]*(n+1)

q = deque([x])
count = 0
while q:
	a = q.popleft()
	visited[a] = 1
	count = count + 1
	for i in A[a]:
		if visited[i] == 0:
			q.append(i)
			visited[i] = 1
print(count)
