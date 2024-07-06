from collections import deque
# check함수 -> 그래프 판별 함수
def check(nd):
    # deque 사용 큐에 입력 노드 넣어줌
    queue = deque()
    queue.append(nd)

    while queue:
        now = queue.pop()
        # 만약 이미 방문한 노드 재방문하면 도넛 그래프
        if visited[now] == True:
            return 1
        # 방문처리
        visited[now] = True
        # 만약 그래프를 돌다가 나가는 간선의 개수가 두 개 이상이면 8자 그래프
        if len(nodes[now]) >=2:
            return 3
        # 현재 node에 연결된 node들을 queue에 넣어줌
        for node in nodes[now]:
            queue.append(node)
    # queue를 다 돌도록 return값이 안 나오면 순환그래프가 아님 -> 막대 그래프
    return 2

def solution(edges):
    global nodes
    global ingoing
    global visited

    #노드의 개수 구하는 부분/ max_node = node의 개수
    max_node = 0
    for edge in edges:
        a,b = edge
        if a>max_node or b>max_node:
            max_node = max(a,b)

    #nodes -> node[index] 에서 나가서 도달하는 node의 리스트
    #ingoing -> node[index]로 가는 간선의 개수
    #visited -> node 방문여부 확인 check(nd)에서 사용
    nodes = [[] for _ in range(max_node+1)]
    ingoing = [0 for _ in range(max_node+1)]
    visited = [False for _ in range(max_node+1)]

    # 위 리스트 초기화하기
    for edge in edges:
        a,b = edge
        nodes[a].append(b)
        ingoing[b]+=1

    #정점 정하는 파트 / start = 정점,들어오는 간선이 없고 & 나가는 간선이 가장 많은 것을 정점으로 진행 / num_outgoing = 나가는 간선의 개수
    start = 0
    num_outgoing = 0
    for i in range(1,max_node+1):
        if ingoing[i] == 0 and len(nodes[i]) > num_outgoing:
            num_outgoing = len(nodes[i])
            start = i
    answer = [start,0,0,0]

    #main 함수 -> check함수로 어떤 그래프인지 판별하고 check함수의 return값을 index로 받아서 +1
    #start node에서부터 시작 / start node는 각 그래프의 무작위 지점과 연결되어 있음
    for node in nodes[start]:
        answer[check(node)]+=1


    return answer