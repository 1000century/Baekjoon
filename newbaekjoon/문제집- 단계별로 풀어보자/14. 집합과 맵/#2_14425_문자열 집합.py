N,M = map(int,input().split())
S = []
check = []
count = 0
for _ in range(N):
    S.append(input())
for _ in range(M):
    if input() in S:
        count = count+1
print(count)