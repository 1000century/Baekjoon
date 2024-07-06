""" 
최대값처리 >>  float("inf") >>> 2332ms 메모리 111332kb
최댓값처리 >> 999999999 >>> 1592ms 메모리 79588kb
"""
import sys
N = int(sys.stdin.readline())
A =[]
for _ in range(2000001):
	A.append(float("inf"))
for _ in range(N):
	x = int(sys.stdin.readline())
	A[x+1000000] =x
for i in range(2000001):
	if A[i] != float("inf"):
		print(A[i])
