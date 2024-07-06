"""
24.03.17 17:13~17:27
lowerbound 개념
"""
N = int(input()) # 주어진 정수

def root(N):

	st = 0
	en = N

	while st <= en:
		mid = (st + en) // 2
		if mid * mid < N:
			st = mid + 1
		else:
			en = mid - 1
	return st

print(root(N))
