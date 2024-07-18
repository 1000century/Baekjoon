## python3로는 뭘해도 시간초과 나와서 pypy로 해보니 시간 맞았음
## 시간단축 관련해 고려해볼 점들
"""
1. input대신 sys.stdin 활용
2. 리스트 대신 set 사용 >> 왜인지는 모름
3. 방향전환 키들은 차라리 하드코딩하는 게 좋다고 하는 듯
"""

import sys

## part1. 문제 조건
R, C = map(int, sys.stdin.readline().split()) #R: 세로길이, C: 가로길이

graph=[[] for _ in range(R)]
for i in range(R):
    graph[i] = list(sys.stdin.readline().strip())

def who_is_my_neighbor(gr,x,y): # 리스트 gr은 R*C 의 크기라고 가정
    neighbor = []
    if x != 0:
        neighbor.append([gr[y][x-1],x-1,y])
    if x != C-1:
        neighbor.append([gr[y][x+1],x+1,y])
    if y != 0:
        neighbor.append([gr[y-1][x],x,y-1])
    if y != R-1:
        neighbor.append([gr[y+1][x],x,y+1])
    return neighbor

def dfs(li, xc, yc, count):
    global answer_count
    depth[ord(graph[yc][xc])-ord('A')] = 1
    count += 1
    answer_count = max(answer_count, count)
    for next in who_is_my_neighbor(li, xc, yc):
        if depth[ord(next[0])-ord('A')] == 0:
            dfs(li, next[1], next[2], count)
    depth[ord(graph[yc][xc])-ord('A')] = 0

depth=[0] * 26 # 알파벳 개수는 26개
count = 0
answer_count = 0
dfs(graph,0,0,0)
print(answer_count)