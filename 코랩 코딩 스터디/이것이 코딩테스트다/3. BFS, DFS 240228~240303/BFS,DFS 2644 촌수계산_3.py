n = int(input())
a,b= map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for li in graph:
    li.sort()

visited= [-1] * (n+1)
def dfs(graph,visited,cur):
    global count,b
    visited[cur] = 0
    count = count + 1
    if b in graph[cur]:
        print(count)
        exit()
    for next in graph[cur]:
        if visited[next] == -1:
            dfs(graph,visited,next)
    count = count -1

count = 0
dfs(graph,visited,a)
print(-1)