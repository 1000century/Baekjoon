# (세현)

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    roota = find(parent,a)
    rootb = find(parent,b)
    if roota<rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb


N = int(input())
parent = {}
for i in range(1,N+1):
    parent[i] = i

map = [["x좌표","y좌표","별번호"]] # 인덱스 1부터 시작이라 인덱스 0은 어떤 값이든 상관없음
for i in range(1,N+1):
    x,y = input().split()
    map.append([float(x),float(y),i])

edges = []
for i in range(1,N+1):
    for j in range(i,N+1):
        dd = (map[i][0]-map[j][0])**2 + (map[i][1]-map[j][1])**2
        d = dd**0.5
        edges.append([d,i,j])

edges.sort()

result = 0
for edge in edges:
    dist,i,j = edge
    if find(parent,i) != find(parent,j):
        union(parent,i,j)
        result = result + dist
print(result)
