# 시도 1) 63%에서 시간초과

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

parent = {}
for i in range(n+1):
	parent[i] = i


for _ in range(m):
	x,a,b = map(int,input().split())
	if x == 0:
		p = min(a,b)
		q = max(a,b)
		pp = set()
		pp.add(p)
		pp.add(q)
		while p != parent[p]:
			p = parent[p]
			if p not in pp:
				pp.add(p)
		while q != parent[q]:
			q = parent[q]
			if q not in pp:
				pp.add(q)
		for i in pp:
			parent[i] = p

	if x == 1:
		while a != parent[a]:
			a = parent[a]
		while b != parent[b]:
			b= parent[b]
		if a ==b:
			print("YES")
		else:
			print("NO")