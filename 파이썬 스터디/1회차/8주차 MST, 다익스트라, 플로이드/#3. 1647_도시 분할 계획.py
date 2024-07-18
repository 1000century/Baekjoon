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

"""
https://www.acmicpc.net/problem/1647
시간제한 2초 >> 2824ms

아이디어
 # 연결된 단 하나의 간선만 끊으면, 2개의 신장트리로 나눌 수 있음.
 # 전체 신장트리에서 가장 긴 간선을 제거한다.
"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = list(range(N))

edges = []
for i in range(M):
	a,b,c = map(int,input().split())
	edges.append((c,a-1,b-1))

edges.sort(key=lambda x:x[0])

result = 0
last = 0
for c,a,b in edges:
	if find(parent,a) != find(parent,b): # 사이클이 생기지 않는다면
		union(parent,a,b) # 같은 부모집합으로
		result = result + c
		last = c 

print(result -last) # 마지막 연결 비용만 빼주기