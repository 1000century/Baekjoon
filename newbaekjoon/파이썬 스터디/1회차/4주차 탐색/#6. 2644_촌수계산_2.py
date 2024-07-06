"""
24.03.28
시도 1) 처음엔 bfs로 풀어도 될 줄 알았는데 안풀림
시도 2) dfs로 느낌으론 풀었지만 재귀 사이의 return 지옥을 해결못해서 답봄

부모노드, 자식노드 구별 해주지 않고 풀어도 되는건가?
"""

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

def dfs(A,now,visited,target,depth =0):
	visited[now] = 1
	if target ==now:
		return depth
	for next in A[now]:
		if visited[next] == 1:
			continue
		if visited[next] == 0:
			result = dfs(A,next,visited,target,depth+1)
			if result != -1:
				return result
	
	return -1

print(dfs(A,x,visited,y))


