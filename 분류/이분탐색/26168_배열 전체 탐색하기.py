"""
24.03.17 01:50~02:11
quiz 1: lowerbound
quiz 2: upperbound

stdin 안쓰면 30점 나왔음
"""
import sys
n, m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
B= []
def quiz(A,q_no,X):
	if q_no ==1: # k보다 크거나 같은 원소 개수
		k = X[1]
		low = 0
		high = len(A)-1 # 열린구간으로 정의
		while low<=high:
			mid = (low+high)//2
			if k>A[mid]:
				low = mid + 1
			else:
				high = mid - 1
		return len(A)-low


	elif q_no ==2:
		k = X[1]
		low = 0
		high = len(A)-1 # 열린구간으로 정의
		while low<=high:
			mid = (low+high)//2
			if k>=A[mid]:
				low = mid + 1
			else:
				high = mid - 1
		return len(A)-low

	else:
		i = X[1]
		low = 0
		high = len(A)-1 # 열린구간으로 정의
		while low<=high:
			mid = (low+high)//2
			if i>A[mid]:
				low = mid + 1
			else:
				high = mid - 1
		begin = low
		
		
		j = X[2]
		low = 0
		high = len(A)-1 # 열린구간으로 정의
		while low<=high:
			mid = (low+high)//2
			if j>=A[mid]:
				low = mid + 1
			else:
				high = mid - 1
		end = low

		return end - begin

for _ in range(m):
	X = list(map(int,sys.stdin.readline().split()))
	print(quiz(A,X[0],X))
