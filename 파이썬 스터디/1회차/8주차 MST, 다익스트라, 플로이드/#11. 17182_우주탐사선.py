"""
우주탐사선
https://www.acmicpc.net/problem/17182
"""
from itertools import permutations
INF = int(1e9)

N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
	for a in range(N):
		for b in range(N):
			graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

ans = INF
temp = [i for i in range(N) if i!=K]

for case in permutations(temp,N-1):
	d = 0
	for i in range(N-1):
		if i != 0:
			d = d + graph[case[i-1]][case[i]]
		else:
			d = d + graph[K][case[i]]
	ans = min(ans,d)

print(ans)