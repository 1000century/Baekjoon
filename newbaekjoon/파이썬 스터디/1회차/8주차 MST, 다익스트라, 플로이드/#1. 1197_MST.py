def find(parent,x):
	if parent[x] == x:
		return x
	parent[x] = find(parent,parent[x]) # 경로압축
	return parent[x]
def union(parent,a,b):
	ra = find(parent,a)
	rb = find(parent,b)
	if ra < rb:
		parent[rb] = ra
	else:
		parent[ra] = rb

import sys
input = sys.stdin.readline

V,E = map(int,input().split())
parent = [0] *(V+1)
edges = []
result = 0

for i in range(1,V+1):
	parent[i] = i

for _ in range(E):
	a,b,c = map(int,input().split())
	edges.append((c,a,b))
edges.sort(key=lambda x:x[0])

for edge in edges:
	c,a,b = edge
	if find(parent,a) != find(parent,b):
		union(parent,a,b)
		result = result + c

print(result)