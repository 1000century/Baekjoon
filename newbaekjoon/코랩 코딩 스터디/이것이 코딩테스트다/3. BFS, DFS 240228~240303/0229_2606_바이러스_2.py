def dfs(graph,x,visited=None,count = 0):
	if visited == None:
		visited = [False] * (len(graph)+1)
	count = count + 1
	visited[x] = True
	if len(graph[x]) ==0:
		return count
	for next in graph[x]:
		if not visited[next]:
			count = dfs(graph,next,visited,count)
	return count

def main():
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]        # N+1 개의 리스트
    for _ in range(M):
        com1,com2=map(int,input().split())
        graph[com1].append(com2)
        graph[com2].append(com1)
    result = dfs(graph,1) - 1 ## 영향받은 거 중에 자기 자신제외
    print(result)

if __name__ == "__main__":
    main()