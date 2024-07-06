"""
24.03.17 19:56~20:03
이분탐색없이 set쓰고 stdin 쓰니까 풀리네
"""
import sys
while True:
	count = 0
	N,M = map(int,sys.stdin.readline().split())
	if N ==0 and M ==0:
		break
	A= set()
	for _ in range(N):
		A.add(int(sys.stdin.readline().rstrip()))
	for _ in range(M):
		x = int(sys.stdin.readline().rstrip())
		if x in A:
			count = count + 1
	print(count)