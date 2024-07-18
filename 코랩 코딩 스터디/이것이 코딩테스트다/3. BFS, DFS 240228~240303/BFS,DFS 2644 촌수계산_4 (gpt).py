
def dfs(graph, x, y, visited=None, depth=0):
    if visited is None:
        visited = [False] * (len(graph) + 1)  # 그래프 크기에 맞춰 방문 배열 초기화
    visited[x] = True  # 현재 노드 방문 표시
    if x == y:  # 목표 노드에 도달했을 경우
        return depth
    for neighbor in graph[x]:  # 현재 노드의 모든 이웃에 대해
        if not visited[neighbor]:  # 아직 방문하지 않은 이웃이 있다면
            result = dfs(graph, neighbor, y, visited, depth + 1)  # 재귀적으로 탐색
            if result != -1:  # 경로를 찾았다면
                return result
    return -1  # y에 도달할 수 없는 경우

def main():
    n = int(input())  # 전체 사람의 수
    x, y = map(int, input().split())  # 촌수를 계산할 두 사람의 번호
    m = int(input())  # 부모 자식들 간의 관계의 개수
    
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    
    # 부모 자식 관계 입력 받기
    for _ in range(m):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        graph[child].append(parent)  # 양방향으로 추가

    ### gpt는 여기에다가 sort를 안했음!!!!
    
    # 촌수 계산
    result = dfs(graph, x, y)
    
    print(result)

if __name__ == "__main__":
    main()
