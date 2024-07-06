"""
N=1일 때 예외처리 중요함
뭔가 dynamic programming이라는 게 있는듯
"""

import sys
input = sys.stdin.readline
N = int(input())
count = 0

def godown(N):
	if N == 1:
		print(0)
	else:
		all = [N]
		before = [N]
		count = 0
		while True:
			next = []
			count = count + 1
			for k in before:
				if k % 2 ==0 and  k//2 not in all:
					next.append(k//2)
					all.append(k//2)
				if k % 3 ==0 and  k//3 not in all:
					next.append(k//3)
					all.append(k//3)
				if k-1 not in all:
					next.append(k-1)
					all.append(k-1)
			if 1 in next:
				print(count)
				break
			else:
				before = next

godown(N)