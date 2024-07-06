"""
최소비용 구하기
https://www.acmicpc.net/problem/1916

전형적인 데익스트라 문제
"""
import heapq
import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
	st,en,c = map(int,input().split())
	graph[st].append((en,c))
s,e = map(int,input().split())

INF = int(1e9)
dist = [INF]*(N+1)
dist[s] = 0
q = []
heapq.heappush(q,(0,s))
while q:
	pd,pn = heapq.heappop(q)
	if dist[pn] < pd:
		continue
	for nn,nc in graph[pn]:
		if nc + pd < dist[nn]:
			dist[nn] = nc+pd
			heapq.heappush(q,(nc+pd,nn))
print(dist[e])