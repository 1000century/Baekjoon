# (세현)
# 2차원 누적합

import sys
input = sys.stdin.readline

R,C,Q = map(int,input().split())
arr = [[0]*(1+C) for _ in range(1+R)]
for r in range(1,1+R):
	for idx,i in enumerate(list(map(int,input().split()))):
		arr[r][idx+1] = i+arr[r-1][idx+1]+arr[r][idx]-arr[r-1][idx]

for _ in range(Q):
	r1,c1,r2,c2 = map(int,input().split())
	cnt = (c2-c1+1)*(r2-r1+1)
	x = arr[r2][c2]-arr[r2][c1-1]-arr[r1-1][c2]+arr[r1-1][c1-1]
	print(x//cnt)