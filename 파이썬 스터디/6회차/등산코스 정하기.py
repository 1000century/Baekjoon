import heapq

INF = int(1e9)

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for s, e, d in paths:
        graph[s].append([e, d])
        graph[e].append([s, d])
    for i in graph:
        graph[i] = sorted(graph[i], key = lambda x:x[1])

    def dijkstra(g):
        distance = [INF] * (n + 1)
        pq = []
        
        heapq.heappush(pq, (0, g))
        distance[g] = 0

        while pq:
            cur_d, node = heapq.heappop(pq)
            if cur_d > distance[node]:
                continue
            for nn, nd in graph[node]:
                next_d = max(cur_d, nd)
                if next_d < distance[nn]:
                    distance[nn] = next_d
                    heapq.heappush(pq, (next_d, nn))

        return distance
    
    # Initialize intensity array with infinite values
    intensity = [INF] * (n + 1)

    # For each gate, compute the minimum intensity to reach all nodes
    for g in gates:
        distance = dijkstra(g)
        for i in range(1, n + 1):
            intensity[i] = min(intensity[i], distance[i])
    
    ans_summit = -1
    ans_dist = INF

    # Find the summit with the smallest intensity
    for summit in sorted(summits):
        if intensity[summit] < ans_dist:
            ans_dist = intensity[summit]
            ans_summit = summit

    return [ans_summit, ans_dist]

# 테스트 예제
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
