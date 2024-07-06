N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]        # N+1 개의 리스트
for _ in range(M):
    num1,num2=map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

## 하위 리스트 오름차순 정렬
for i in range(N+1):
    graph[i].sort()

visit = [False] * (N+1)

def dfs(current): # c current
    ans_dfs.append(current)
    visit[current] = True
    for n in graph[current]:
        if visit[n]==0:
            dfs(n)

ans_dfs = []
dfs(1)
print(len(ans_dfs)-1)

