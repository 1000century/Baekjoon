"""
시도 1) 시간초과
시도 2) 이해는 정확히 안됨..
일단은 rank는 나보다 큰사람의 수를 센거 같음
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

INF = int(1e9)
rank = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1,N+1):
	rank[a][a] = 0

for _ in range(M):
	a,b = map(int,input().split())
	rank[a][b] = 1

for k in range(1,N+1):
	for a in range(1,N+1):
		for b in range(1,N+1):
			rank[a][b] = min(rank[a][b], rank[a][k] + rank[k][b])

count =0 
for i in range(1,N+1):
	for j in range(1,N+1):
		right = True
		if rank[i][j] == INF and rank[j][i] == INF:
			right = False
			break
	if right == True:
		count = count + 1

print(count)