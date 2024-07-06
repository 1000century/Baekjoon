"""
시도 1) 시간초과
시도 2) 이해는 정확히 안됨..
일단은 rank는 나보다 큰사람의 수를 센거 
시도 3) 모르겠다모르겠다
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

INF = int(1e9)
rank = [[] for _ in range(N+1)]

for _ in range(M):
	a,b = map(int,input().split())
	rank[a].append(b)

for now in range(1,N+1):
	q = deque([now])
	while q:
		x = q.popleft()
		for next in rank[x]:
			if next not in rank[x]:
				rank[a].append(next)
				q.append(next)

print(rank)
count = 0
for i in range(1,N+1):
	if len(rank[i]) + 1 == i:
		count = count + 1
print(count)