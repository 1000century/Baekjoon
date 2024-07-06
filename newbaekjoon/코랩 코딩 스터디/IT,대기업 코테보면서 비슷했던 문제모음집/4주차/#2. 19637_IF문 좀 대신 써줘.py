# (세현)

import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_left

"""
https://www.acmicpc.net/problem/19637
"""
def test():
	N, M = map(int,input().split())
	group = []
	name = {}
	for i in range(N):
		a,b = input().split()
		name[i] = a
		group.append(int(b))
	for _ in range(M):
		print(name[bisect_left(group,int(input()))])
		print('\n')
test()