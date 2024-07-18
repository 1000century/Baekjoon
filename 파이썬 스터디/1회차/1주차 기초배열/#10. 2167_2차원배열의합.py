
"""
09:05~09:30 시간초과
pypy로 하니까 시간초과 안생김 3428ms
이중루프를 단일 루프로 하니까 그냥 python으로 해도 시간초과 해결됨 7248ms
09:30~09:37
"""
import sys
N, M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
	arr.append(list(map(int,sys.stdin.readline().split())))


K = int(sys.stdin.readline())

for _ in range(K):
	ia,ja,xa,ya = map(int,sys.stdin.readline().split())
	i = ia-1
	j = ja-1
	x = xa-1
	y = ya-1

	sume = 0
	for p in range(i,x+1):
		sume = sume + sum(arr[p][j:y+1])
	print(sume)




