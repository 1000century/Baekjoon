N,M = map(int,input().split())

floor = []

for _ in range(N):
	x = list(input())
	floor.append(x)

visited = [[0]*M for _ in range(N)]

def dfs(x,y,shape):
	if visited[y][x] ==1:
		return
	if floor[y][x] != shape:
		return
	else:
		visited[y][x] = 1
		if shape == "|":
			if floor[y][x] == "|" and y<N-1:
				dfs(x,y+1,"|")
		elif shape == "-":
			if floor[y][x] == "-" and x<M-1:
				dfs(x+1,y,"-")
count = 0
for j in range(N):
	for i in range(M):
		if visited[j][i] == 0:
			count = count + 1
			dfs(i,j,floor[j][i])
print(count)


	

	
