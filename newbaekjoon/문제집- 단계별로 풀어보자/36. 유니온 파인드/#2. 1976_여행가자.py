N = int(input())
M = int(input())

def find(x):
	if x != parent[x]:
		parent[x] = find(parent[x])
	return parent[x]

def union(a,b):
	a = find(a)
	b = find(b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

parent = {}
for i in range(N):
	parent[i] = i

for i in range(N):
	X = list(map(int,input().split()))
	for j in range(N):
		if X[j] == 1:
			union(i,j)

trip = list(map(int,input().split()))

before = parent[trip[0]-1]
isit = "YES"
for i in range(len(trip)):
	next = trip[i]-1
	if before != parent[next]:
		isit = "NO"
print(isit)
