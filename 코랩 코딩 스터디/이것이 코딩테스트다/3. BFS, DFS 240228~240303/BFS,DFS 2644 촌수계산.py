## part1. 문제 조건
n = int(input())              # 전체 사람수
a,b=map(int,input().split())  # 촌수 계산해야 하는 사람
a, b = min(a, b), max(a, b)
m = int(input())              # 주어진 관계(작대기) 개수

base=[[] for _ in range(n+1)]       # 첫칸은 빈칸으로 설정
for _ in range(m):
    num1,num2=map(int,input().split())
    base[num1].append(num2)
    base[num2].append(num1)

# 안쪽 리스트 오름차순 배열
for i in range(n+1):
    base[i].sort()

answer = -1

def bfs(s,e): # s start
    q = [s]
    v[s] = 1
    while len(q) != 0:
        c = q.pop(0)
        for next in base[c]:
            if v[next]==0:
                q.append(next)
                v[next] = v[c] + 1
                if next == e:
                    return v[next]-1
    return -1
                

v=[0]*(n+1)
print(bfs(a,b))