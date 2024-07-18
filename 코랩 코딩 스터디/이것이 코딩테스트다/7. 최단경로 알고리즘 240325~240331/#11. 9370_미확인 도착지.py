import heapq
T = int(input())

def djikstra(n,m,t):
	graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
	s,g,h = map(int,input().split())
	for _ in range(m):
		a,b,d = map(int,input().split())
		graph[a][b] = d
		graph[b][a] = d
	for _ in range(t):
		x = int(input())

	q = 



for _ in range(T):
	n,m,t = map(int,input().split())
	djikstra(n,m,t)