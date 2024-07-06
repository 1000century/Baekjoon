import sys
sys.setrecursionlimit(1000000000)

def dfs(graph, x,y,visited,W,H):
	visited[y][x] = 1
	for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(1,-1),(-1,1),(-1,-1)]:
		nx, ny = x + dx, y + dy
		if 0 <= nx < W and 0 <= ny < H and visited[ny][nx] == 0 and graph[ny][nx] == 1:
			dfs(graph,nx,ny,visited,W,H)

def solve(W,H):
	count = 0
	visited = [[0]*W for _ in range(H)]
	bigmap = [list(map(int,input().split())) for _ in range(H)]
	for j in range(H):
		for i in range(W):
			if visited[j][i] == 0 and bigmap[j][i] == 1:
				count = count + 1
				dfs(bigmap,i,j,visited,W,H)
	return count

while True:
	w, h = map(int, input().split())
	if w == h == 0:
		break
	print(solve(w,h))
