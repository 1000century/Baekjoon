"""
24.03.17 17:32~17:37

이분탐색보다는 set으로 푸는 게 더 좋은듯
"""
T = int(input())

def memorize(A,B):
	for b in B: # B에 있는 원소 b에 대하여~
		if b in A:
			print(1)
		else:
			print(0)

for _ in range(T):
	N = int(input()) # 수첩 1
	A = set(map(int,input().split()))

	M = int(input()) # 수첩 2
	B = list(map(int,input().split()))

	memorize(A,B)
