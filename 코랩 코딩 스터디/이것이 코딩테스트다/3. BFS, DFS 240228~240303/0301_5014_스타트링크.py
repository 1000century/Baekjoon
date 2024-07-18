"""
*** 리스트 복사할 때 주의점
(O) visited = [[False for _ in range(N)] for _ in range(N)]
(X) visited =[False for _ in range(N)]*N

*** 2차원 리스트에서 가장 큰수 찾는 법
>> max_value = max(max(row) for row in graph)

BFS는 큐에서 뺀 다음이 아닌, 큐에 넣을 때 방문 체크를 해야 중복 방문이 일어나지 않습니다.


왜 맞음??????????
초반 부분 왜 성공했는지 모르겠다.
걸린시간: 12:53~14:33
"""

# (세현)
import sys
from collections import deque
F,S,G,U,D = map(int, sys.stdin.readline().split())

if S == G:
    print(0)
    exit()

if U == 0 and S < G or D == 0 and S > G:
    print("use the stairs")
    exit()
    

# 총 F층, S>G, 올라가는 단위(U) 내려가는 단위(D)
visited = [0 for _ in range(F+1)]

count = "use the stairs"
def bfs(current, end):
    global count
    queue = deque([[current,0]])
    visited[current] = True

    while queue:
        x, y = queue.popleft()
        if x == end:
            count = y
            break
        if x + U <= F and  visited[x+U] == 0:
            queue.append([x+U, y+1])
            visited[x+U] = 1
        if x - D >= 1 and  visited[x-D] == 0:
            queue.append([x-D, y+1])
            visited[x-D] = 1
if __name__ == "__main__":    
    bfs(S,G)
    print(count)