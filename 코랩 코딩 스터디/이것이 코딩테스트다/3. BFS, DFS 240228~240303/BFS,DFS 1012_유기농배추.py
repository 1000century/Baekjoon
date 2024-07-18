## 재귀 깊이 한계를 원래는 넘었는데 sys.setrecursionlimit 해서 바꿈
"""
dfs 함수 구성요소
1. 재귀표현
2. 변수 설정할 때 현재 시점을 나타내는 것이 필요(ex. current)
"""

import sys
import copy

sys.setrecursionlimit(10**6) ### 재귀 깊이 한계 바꾸기


## part1. 문제 조건
T = int(sys.stdin.readline())     # 테스트 개수

## Part2. 함수 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global worm
    visited[y][x] = 1
    if batt[y][x]:
        batt[y][x] = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                dfs(nx, ny)  # 다음 칸으로 이동

## Part 3 변수 입력 및 실행
for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().split()) # M*N(가로,세로) K(배추개수)

    batt=[[False] * M for _ in range(N)]           # 배추밭 만들기
    visited = copy.deepcopy(batt)             # 방문했는지 보는 리스트

    for i in range(K):
        x,y = map(int, sys.stdin.readline().split())
        batt[y][x] = True                          # 배추밭에 배추 심기

    worm = 0                                       # 지렁이 개수 초기화
    
    for b in range(N):
        for a in range(M):
            if batt[b][a] == 1:
                worm = worm + 1
            dfs(a,b)
    print(worm)

