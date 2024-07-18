import sys
input = sys.stdin.readline

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

def test(X):
	m,n = map(int,X.split())
	edges = []
	for _ in range(n):
		a,b,c = map(int,input().split())
		edges.append((c,a,b))
	edges.sort()

	parent = [i for i in range(m+1)]
	ans = 0

	for edge in edges:
		cost,va,vb = edge
		if find(parent,va) != find(parent,vb):
			union(parent,va,vb)
		else:
			ans = ans + cost

	print(ans)

while True:
	X = input()
	if X =="0 0\n":
		break
	else:
		test(X)
