"""
학교 탐방하기
https://www.acmicpc.net/problem/13418

시도 1) dfs
시도 2) 크루스칼 알고리즘

## edges sort 안해줘도 됨..(why?)
"""

def find(parent,x):
	if parent[x] == x:
		return x
	parent[x] = find(parent,parent[x])
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

N,M = map(int,input().split())
edges = []
for _ in range(M+1):
	A,B,C = map(int,input().split())
	edges.append((C,A,B))

parent_best = [i for i in range(N+1)]
parent_worst = [i for i in range(N+1)]
best = N
worst = 0

for c,a,b in edges:
	# 최선
	if c ==1:
		if find(parent_best,a) != find(parent_best,b):
			union(parent_best,a,b)
			best = best -1
	
	# 최악
	else:
		if find(parent_worst,a) != find(parent_worst,b):
			union(parent_worst,a,b)
			worst = worst + 1
		

print(worst**2-best**2)
