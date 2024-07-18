"""
시작시간 : 24.03.10 16.58 ~ 20:56 (성공)

sys.stdout.wrtie 는 좀 에바네

시도 2 : 21:01~
딴 사람 꺼 보고 그대로 쓴거임..
"""
# (세현)
import sys

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A.sort()

def binary(A,k):
	start = 0
	end = N-1

	while start <= end:
		mid = (start + end) //2
		if k < A[mid]:
			end = mid -1
		elif k == A[mid]:
			return 1
		else:
			start = mid + 1
	return 0

for element in B:
# N = 5 라면 (2 /3) > ()
	if element >A[-1] or element < A[0]:
		print(0)
	else:
		print(binary(A,element))
