"""
기본적으로 bfs 함수 정의하는 데에 9줄이 필요함
1. 함수 정의 / 2. queue 함수만들기 / 3. 방문처리
4. while문 시작 / 5. 선입선출처리(current)
6. for문 시작 graph[current] / 7. next node 방문여부 확인 / 8,9. queue에 append 후 방문처리

몇 번 지나쳤는지 확인하는 요소, 즉 정답 print하는 것은 주로 방문처리 함수를 잘 만들어야 함
A. 방문처리 함수를 단순 false or true 개념으로 할지
B. 아니면 distance 개념으로 넣을지
"""

# (세현)
from collections import deque

def main():
    N,M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    dist = bfs(graph,1)       # 반드시 함수의 변수 모두 넣지 않아도 됨
    M = max(dist)
    print(f"{dist.index(M)} {M} {dist.count(M)}")

def bfs(graph,x,dist=None):                     # bfs 만들때 필수문장(1/9)
    if dist == None:          # 방문 함수 초기화 (위에서 해도 됨)
        dist = [-1] * (len(graph)+1)
    queue = deque([x])                          # bfs 만들때 필수문장(2/9)
    dist[x] = 0                                 # bfs 만들때 필수문장(3/9)
    while queue:                                # bfs 만들때 필수문장(4/9)
        current = queue.popleft()               # bfs 만들때 필수문장(5/9)
        for next in graph[current]:             # bfs 만들때 필수문장(6/9)
            if dist[next] == -1:                # bfs 만들때 필수문장(7/9)
                dist[next] = dist[current] + 1  # bfs 만들때 필수문장(8/9)
                queue.append(next)              # bfs 만들때 필수문장(9/9)
    return dist               # 정답 출력 위해서 return 

# main함수 여러번쓰면 터미널에서 예제 테스트에서 한번에 여러개 가능
# 아래 두 줄 복사해서 두 번 쓰면 예제 2개 테스트 가능. 세 번 쓰면 예제 3개 테스트 가능
if __name__ == "__main__":
    main()