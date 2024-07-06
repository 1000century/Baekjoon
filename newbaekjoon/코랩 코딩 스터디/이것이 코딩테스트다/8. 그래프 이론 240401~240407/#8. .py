import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

parent = [x for x in range(n)]

def find(x):
	if x == parent[x]:
		return x
	else:
		parent[x] = find(parent[x])
		return parent[x]
def union(x, y):
	parent_x = find(x)
	parent_y = find(y)
	if parent_x < parent_y:
		parent[parent_y] = parent_x
	else:
		parent[parent_x] = parent_y
out = 0

for turn in range(1, m + 1):
	cin, cout = list(map(int, input().split()))
	if find(cin) == find(cout):
		out = turn
		break
	union(cin, cout)

print(out)