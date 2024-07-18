# (세현)
# 2차원 누적합
import sys
N, M = map(int,sys.stdin.readline().split())
A = []
for _ in range(N):
	A.append(list(map(int,sys.stdin.readline().split())))

sume = [[0]*(N+1) for _ in range(N+1)]
hap = 0
for i in range(1,N+1):
	for j in range(1,N+1):
		sume[i][j] = (A[i-1][j-1]
					+ sume[i-1][j]
					+ sume[i][j-1]
					- sume[i-1][j-1])

for _ in range(M):
	x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
	ans = (sume[x2][y2]
		- sume[x2][y1-1]
		- sume[x1-1][y2]
		+ sume[x1-1][y1-1])
	print(ans)