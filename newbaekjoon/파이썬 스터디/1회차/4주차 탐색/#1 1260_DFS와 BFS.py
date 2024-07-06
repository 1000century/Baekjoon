from collections import deque

N,M,V = map(int,input().split())

connection = [[] for _ in range(N)]
for _ in range(M):
	a,b = map(int,input().split())
	connection[a-1].append(b-1)
	connection[b-1].append(a-1)

# 하위 리스트 정렬
for i in range(N):
	connection[i] = sorted(connection[i])


# dfs
def dfs(connection,visited,q):
	now = q.pop()
	visited[now] = 1
	ans.append(now+1)
	for next in connection[now]:
		if visited[next] == 0:
			q.append(next)
			dfs(connection,visited,q)
ans=[]
visited = [0]*N
q = [V-1]
dfs(connection,visited,q)
print(*ans)


# bfs
ans = []
def bfs(connection,visited,q):
	now = q[0]
	visited[now] = 1
	ans.append(now+1)
	while q:
		now = q.popleft()
		for next in connection[now]:
			if visited[next] == 0:
				ans.append(next+1)
				visited[next] = 1
				q.append(next)
ans = []
visited = [0]*N
q = deque([V-1])
bfs(connection,visited,q)
print(*ans)


