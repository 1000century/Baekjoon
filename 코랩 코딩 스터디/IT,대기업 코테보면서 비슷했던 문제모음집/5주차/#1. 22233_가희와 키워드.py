# (세현)

import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
keyword = set()
for _ in range(N):
	keyword.add(input().rstrip())
for _ in range(M):
	for i in list(input().rstrip().split(",")):
		keyword.discard(i)
	print(len(keyword))