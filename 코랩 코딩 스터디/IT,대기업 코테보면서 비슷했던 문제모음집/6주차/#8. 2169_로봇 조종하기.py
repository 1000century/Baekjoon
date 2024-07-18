from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
INF = int(1e9)
N,M = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1,M):
	arr[i] = arr[i-1]+arr[i]
for _ in range(N-1):
	mars = list(map(int,input().split()))
	temp = []
	for i in range(M):
		kk = [0]*M
		for k in range(M):
			if k ==i:
				kk[k] = arr[k] + mars[k]
			elif k < i:
				kk[k] = arr[k] + sum(mars[k:i+1])
			else:
				kk[k] = arr[k] + sum(mars[i:k+1])
		temp.append(max(kk))
	arr = temp
	print(arr)
print(arr[-1])



