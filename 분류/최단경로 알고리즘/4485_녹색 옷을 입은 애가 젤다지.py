import heapq
INF = int(1e9)

def djikstra(N,num):
	graph = [list(map(int,input().split())) for _ in range(N)]
	ways = [[INF]*(N) for _ in range(N)]

	X = []
	heapq.heappush(X,(graph[0][0],0,0))
	ways[0][0] = graph[0][0]

	while X:
		money,x,y = heapq.heappop(X)

		if x==N-1 and y == N-1:
			print(f"Problem {num}: {money}")
			break
		for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=nx<N and 0<=ny<N:
				temp = money+graph[nx][ny]
				if temp < ways[nx][ny]:
					ways[nx][ny] = temp
					heapq.heappush(X,(temp,nx,ny))
	



num = 0
while True:
	N = int(input())
	num = num + 1
	if N == 0:
		break
	djikstra(N,num)
	


