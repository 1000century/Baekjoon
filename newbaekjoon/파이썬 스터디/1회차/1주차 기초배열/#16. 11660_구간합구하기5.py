"""
11:19~11:43 pyp3로 푸니까 시간초과 안뜸
"""
import sys
N, M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
	arr.append(list(map(int,sys.stdin.readline().split())))

sume = []
for _ in range(N+1):
	sume.append([0]*(N+1))

for i in range(1,N+1):
	for j in range(1,N+1):
		sume[i][j] = sume[i][j-1]+arr[i-1][j-1]

for _ in range(M):
	x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
	hap = 0
	for x in range(x1,x2+1):
		hap = hap + sume[x][y2]-sume[x][y1-1]
	print(hap)