N,M = map(int,input().split())

def back(N,M,arr):
	if len(arr) == M:
		print(*arr)
		return 
	for i in range(1,N+1):
		if visited[i] ==0:
			arr.append(i)
			visited[i] = 1
			back(N,M,arr)
			arr.pop()
			visited[i] = 0

visited = [0]*(N+1)
	
back(N,M,[])