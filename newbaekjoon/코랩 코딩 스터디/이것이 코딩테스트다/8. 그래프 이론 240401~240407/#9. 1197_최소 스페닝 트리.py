import sys
input = sys.stdin.readline

V,E = map(int, input().split())

edges = []
for i in range(E):
	a,b,c = map(int,input().split())
	edges.append((c,a,b))
edges.sort()

def find(parent,x):
	if parent[x] != x:
		parent[x] = find(parent,parent[x])
	return parent[x]

def union(parent,a,b):
	x = find(parent,a)
	y = find(parent,b)
	if x < y:
		parent[y] = x
	else:
		parent[x] = y

parent = [i for i in range(V+1)]
ans = 0

for edge in edges:
	cost,va,vb = edge
	if find(parent,va) != find(parent,vb):
		union(parent,va,vb)
		ans = ans + cost

print(ans)