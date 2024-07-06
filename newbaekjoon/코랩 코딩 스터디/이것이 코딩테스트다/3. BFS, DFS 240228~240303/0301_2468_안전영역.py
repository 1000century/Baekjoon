"""
*** 리스트 복사할 때 주의점
(O) visited = [[False for _ in range(N)] for _ in range(N)]
(X) visited =[False for _ in range(N)]*N

*** 2차원 리스트에서 가장 큰수 찾는 법
>> max_value = max(max(row) for row in graph)

"""

# (세현)
from collections import deque

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

max_value = max(max(row) for row in graph)


def high(height,visited, max_num):
    for i in range(N):
        for j in range(N):
            if height[j][i] <= max_num:
                visited[j][i] = True

def bfs(x, y, visited):
    queue = deque([[x,y]])
    visited[y][x] = True  ## 방문함수 on
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # nx, ny가 그래프 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([nx, ny])

answer = []
for h in range(0,max_value):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    high(graph,visited,h)
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                bfs(i,j,visited)
                count = count + 1
    answer.append(count)

print(max(answer))

