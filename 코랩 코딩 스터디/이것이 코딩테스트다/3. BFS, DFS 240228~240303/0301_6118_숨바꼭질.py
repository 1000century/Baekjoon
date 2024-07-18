"""
*** 리스트 복사할 때 주의점
(O) visited = [[False for _ in range(N)] for _ in range(N)]
(X) visited =[False for _ in range(N)]*N

*** 2차원 리스트에서 가장 큰수 찾는 법
>> max_value = max(max(row) for row in graph)

걸린시간: 14:37 ~ 15:05(DFS로 잘못풀었다는 걸 느낌) ~15:23(1차 제출) ~15:33(최종)
"""
import sys
from collections import deque
N,M = map(int, sys.stdin.readline().split())

hut = [[] for _ in range(0,N+1)]
for _ in range(1,M+1):
    a,b = list(map(int, sys.stdin.readline().split()))
    hut[a].append(b)
    hut[b].append(a)

for i in hut:
    i.sort()


visited = [False] * (N+1)
count = [False] * (N+1)

def bfs(v):
    queue = deque([[v,0]])
    visited[v] = True
    while queue:
        v,dist = queue.popleft()
        for i in hut[v]:
            if not visited[i]:
                queue.append([i,dist+1])
                count[i] = dist+1
                visited[i] = True


bfs(1)

m = max(count)
print(count.index(m), m, count.count(m))


