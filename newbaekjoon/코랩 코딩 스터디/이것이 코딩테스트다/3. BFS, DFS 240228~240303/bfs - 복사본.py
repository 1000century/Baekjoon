
## 변수 설정
N, M, V = map(int, input().split())
base=[[] for _ in range(N+1)]

for _ in range(M):
    num1,num2=map(int,input().split())
    base[num1].append(num2)
    base[num2].append(num1)

## 하위 리스트 오름차순 정렬
for i in range(N+1):
    base[i].sort()

def dfs(c): # c current
    ans_dfs.append(c)
    v[c] = 1
    for n in base[c]:
        if v[n]==0:
            dfs(n)

def bfs(s): # s start
    q = []
    q.append(s)  ############# 시작점이 3이라면
    ans_bfs.append(s)
    v[s] = 1

    while len(q) != 0:
        c = q.pop(0) ######### 3 보다 딱 한단계 아래의 것들 전부 처리
        for n in base[c]:
            if v[n]==0:
                q.append(n)  ####### 그러다가 새로운 q가 나오면(선입선출식으로)
                                ####  for문 끝나고 다시 while문으로 돌아감
                ans_bfs.append(n)
                v[n] = 1

v=[0]*(N+1)
ans_dfs = []
dfs(V)

v=[0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)