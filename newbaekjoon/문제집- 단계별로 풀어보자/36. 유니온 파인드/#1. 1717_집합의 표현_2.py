"""
시도 1) 63%에서 시간초과
시도 2) 경로압축 시행했지만 find 함수에서 계속 recursion error, 시간초과 나옴

def find(p):
	if p != parent[p]:
		parent[p] = find(parent[p])
	return parent[p]

마지막 문장을 return find(parent[p]) 하면 재귀깊이 에러 + 시간초과 뜸
시도 3) find 함수 마지막 문장 고치다 보니 해결됨
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find(p):
	if p != parent[p]:
		parent[p] = find(parent[p])
	return parent[p] #

def union(a,b):
	a = find(a)
	b = find(b)
	if a <b:
		parent[b] = a
	else:
		parent[a] = b

n,m = map(int,input().split())

parent = {}
for i in range(n+1):
	parent[i] = i

for _ in range(m):
	x,a,b = map(int,input().split())
	if x == 0:
		union(a,b)
	else:
		if find(a) == find(b):
			print("YES")
		else:
			print("NO")