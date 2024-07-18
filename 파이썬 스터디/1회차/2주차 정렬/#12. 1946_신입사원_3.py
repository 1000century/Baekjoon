"""
이중포문 >> 시간초과..

최솟값 함수 >> 시간초과
for i in range(1,N+1):
	if min(X[1:i+1])==X[i]:
		count = count + 1

여기서 standardinput 안쓰면 시간초과

한번 함수 없이 써보자. 함수없이 써보면 1912ms > > 2272ms 시간 증가됨..
함수로 쓰는 게 이득
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
	count = 1
	mini = X[1]
	for i in range(1,N+1):
		if X[i] < mini:
			mini = X[i]
			count = count + 1
	print(count)

