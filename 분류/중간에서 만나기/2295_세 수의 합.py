# 시도 여러번 후) 질문게시판을 찾아보다가 해보니 pypy로만 통과

import sys
input = sys.stdin.readline

N = int(input())
U = list(int(input()) for _ in range(N))
U.sort()

for t in range(N-1,-1,-1):
	target = U[t]
	for x in range(t-1,-1,-1):
		a = U[x]
		for y in range(x,-1,-1):
			b = U[y]
			if a +b>target:
				continue
			for z in range(y,-1,-1):
				c = U[z]
				if a + b+c >target:
					continue
				if a+b+c == target:
					print(target)
					exit()