"""
이중포문 >> 시간초과..
"""

import sys
T = int(sys.stdin.readline().rstrip())

def how_many(X,N):
	count = N
	for i in range(1,N+1):
		for j in range(1,i):
			if X[i]>X[j]: #만약 너가 둘다 못하면
				count = count -1
				break
	return count


for _ in range(T):
	N = int(sys.stdin.readline().rstrip())
	X = [0]*(N+1)
	for i in range(N):
		a,b = map(int,sys.stdin.readline().split())
		X[a] = b
	print(how_many(X,N))

