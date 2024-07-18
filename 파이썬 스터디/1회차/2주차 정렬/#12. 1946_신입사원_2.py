"""
이중포문 >> 시간초과..

최솟값 함수 >> 시간초과
for i in range(1,N+1):
	if min(X[1:i+1])==X[i]:
		count = count + 1

여기서 standardinput 안쓰면 시간초과
"""

import sys
T = int(sys.stdin.readline().rstrip())

def how_many(X,N):
	count = 1
	mini = X[1]
	for i in range(1,N+1):
		if X[i] < mini:
			mini = X[i]
			count = count + 1
	return count


for _ in range(T):
	N = int(sys.stdin.readline().rstrip())
	X = [0]*(N+1)
	for i in range(N):
		a,b = map(int,sys.stdin.readline().split())
		X[a] = b
	print(how_many(X,N))

