N = int(input())

normal, abnormal = [], []

for _ in range(N):
	X = input()
	n = []
	ab = []
	for x in X:
		n.append(x)
		if x == "G":
			ab.append("R")
		else:
			ab.append(x)
	normal.append(n)
	abnormal.append(ab)

def colorcount(N,group):
	visited = [[0]*(N+1) for _ in range(N)]
	count = 0
	for i in range(N):
		for j in range(N):
			if visited[i][j] ==0:
				count = count + 1
				visited[i][j] = 1
				stack=[[i,j]]
				while stack:
					x,y = stack.pop()
					for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
						if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
							if group[x][y] == group[nx][ny]:
								visited[nx][ny] = 1
								stack.append([nx,ny])
	return count

print(colorcount(N,normal), colorcount(N,abnormal))
