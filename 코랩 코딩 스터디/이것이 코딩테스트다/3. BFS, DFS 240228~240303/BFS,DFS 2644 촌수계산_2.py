"""
@@@@ 순서
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단노드 빼기 전에 인접노드 방문여부 확인 후 재귀
3. 끝날때까지

함수밖에서 할 일 / 함수 위아래 어디에 쓰는지는 크게 상관없는 듯
- 기본적인 input 정리
- input 중에서 가장 중요한 '인접리스트'방식이냐 '인접행렬'방식 결정여부는 따로 빼서 설명
- 방문정보리스트 만들기 visited = [False] * 12

어떤 방식으로 초기화할지 >> 인접리스트 방식을 개인적으로 선호
- '인접리스트' 방식으로 초기화 하는 법 >> [[] for _ in range(m)]
- range(m) 으로 할지 range(m+1) 로 할지 고민해보자
- 반드시 하위 리스트는 sort 해주어야 함. >> 하위리스트다 보니까 for문 써야함

함수 안에서 할일
 - 현재노드 방문 처리 > (print 관련한 처리) > 인접노드 각각을 for 문으로 처리
 - 따라서 필수적으로 필요한 문장은 전부 다 해서 5문장 밖에 안됨

함수의 변수 설정 관련
 - graph >>> 뭔가 global선언하듯이 하는듯?
 - 방문정보리스트 >>> visited, time_is_gold 등으로 표시
 - 현재노드 >>> graph, v, base 등으로 표시
"""
"""
반례
10
7 6
9
1 2
1 3
1 4
9 1
9 10
3 5
3 6
2 7
2 8
<탐색순서>
정답 코드 : [7, 2, 1, 3, 6, 5, 4, 9, 10, 8]
잘못된 코드: [7, 2, 1, 3, 5, 6, 4, 9, 10, 8]

2
2 1
1
1 2
"""
import copy
n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
	x,y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)
for i in range(n+1):
    graph[i].sort()

visited = [-1] * (n+1)

def dfs(cur,visited,dist):
    visited[cur] = dist
    for next in graph[cur]:
        if visited[next] == -1:
            dfs(next,visited,dist+1)

dfs(a,visited,0)
print(visited[b])

