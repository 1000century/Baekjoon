"""
위상정렬
1. 정점 초기화
2. 간선 계산
3. 큐에 삽입
4. 위상정렬과정
"""


import sys
input = sys.stdin.readline
from collections import deque

def test():
	N, M = map(int,input().split())
	D = [0]+list(map(int,input().split()))

	indegree = [0] * (N+1)
	edges = [[] for _ in range(N+1)]
	for _ in range(M):
		a,b = map(int,input().split())
		edges[a].append(b)
		indegree[b] = indegree[b] + 1 

	W = int(input().rstrip())
	ans = D[:]

	rank = deque([])


	for i in range(1,N+1):
		if indegree[i] == 0:
			rank.append(i)

	while rank:
		now = rank.popleft()
		for i in edges[now]:
			ans[i] = max(ans[i],ans[now]+D[i])
			indegree[i] = indegree[i]-1
			if indegree[i] == 0:
				rank.append(i)
	print(ans[W])


T = int(input())
for _ in range(T):
	test()

