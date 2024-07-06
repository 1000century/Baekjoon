def find(parent,x): # 부모 노드 찾기
	if parent[x] == x:
		return x
	parent[x] = find(parent,parent[x])
	return parent[x]
def union(parent,a,b): # 부모 노드 합치기
	ra = find(parent,a)
	rb = find(parent,b)
	if ra < rb:
		parent[rb] = ra
	else:
		parent[ra] = rb

import sys
input = sys.stdin.readline

N = int(input().rstrip())
parent = list(range(N))

edges = []

for i in range(N):
	temp = list(map(int,input().split()))
	for j in range(i+1,N):
		edges.append((temp[j],i,j))
edges.sort(key=lambda x:x[0])

result = 0
for c,a,b in edges:
	if find(parent,a) != find(parent,b): # 사이클이 생기지 않는다면
		union(parent,a,b) # 같은 부모집합으로
		result = result + c
print(result)