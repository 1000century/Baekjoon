# pypy3로만 통과
# rstrip 안쓰면 틀림
# 딕셔너리 구조를 반대로 해야함 각 문자열 인덱스를 key로 해야함

import sys
input = sys.stdin.readline

S = list(input().rstrip())
Z = {0:[0]*26}

for i,s in enumerate(S):
	Z[i+1]=Z[i][:] # [:] 필수!
	Z[i+1][ord(s)-97] = Z[i+1][ord(s)-97]+ 1
q = int(input().rstrip())
for _ in range(q):
	a,l,r = input().split()
	l = int(l)
	r = int(r)
	ans = Z[r+1][ord(a)-97] - Z[l][ord(a)-97]
	print(ans)
