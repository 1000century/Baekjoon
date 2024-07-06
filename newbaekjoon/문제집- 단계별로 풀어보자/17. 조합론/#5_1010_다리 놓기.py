T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    result = 1
    for i in range(M-N+1, M + 1):
        result = result * i
    div = 1
    for j in range(1,N+1):
        div= div * j
    print(result//div)
## 그냥 조합이다 이놈아 중복조합 이런거 아니야