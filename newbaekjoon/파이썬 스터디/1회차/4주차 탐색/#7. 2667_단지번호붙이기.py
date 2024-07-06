"""
24.03.28 return 헷갈려서 그냥 전역변수 씀...
"""
N = int(input())

village = [list(map(int,input().replace(""," ").split())) for _ in range(N)]

def dfs(graph,visited,x,y,N,depth=0):
	global result
	visited[x][y] = 1
	for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
		nx,ny = x+dx,y+dy
		if 0<=nx<N and 0<=ny<N:
			if visited[nx][ny] == 1 or graph[nx][ny]==0:
				visited[nx][ny] = 1
				continue
			else:
				result = result + 1
				dfs(village,visited,nx,ny,N,depth+1)

visited = [[0]*N for _ in range(N)]

count = 0
ans = []
for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			if village[i][j] == 0: # 더 들어갈 필요가 없으니 걍 방문처리하고 끝
				visited[i][j] = 1
			else:
				result = 1
				count = count + 1
				dfs(village,visited,i,j,N,0)
				ans.append(result)
print(count)
ans.sort()
print(*ans,sep='\n')
