"""
시도 1) 시간초과
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
rank = [[[],[]] for _ in range(N+1)]
for _ in range(M):
	a,b = map(int,input().split())
	rank[a][0] = rank[a][0] + [b]
	rank[b][1] = rank[b][1] + [a]

for k in range(1,N+1):
	for a in range(1,N+1):
		for ele in rank[a][0]:
			if a in rank[k][0]:
				if ele in rank[k][0]:
					continue
				rank[k][0] = rank[k][0] + [ele]
		for ele in rank[a][1]:
			if a in rank[k][1]:
				if ele in rank[k][1]:
					continue
				rank[k][1] = rank[k][1] + [ele]


count = 0
for i in range(1,N+1):
	if len(rank[i][1]) + len(rank[i][0]) ==N-1:
		count = count + 1
print(count)
