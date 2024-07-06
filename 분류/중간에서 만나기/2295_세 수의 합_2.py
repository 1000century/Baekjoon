# 시도 여러번 후) 질문게시판을 찾아보다가 해보니 pypy로만 통과
# 시도 2) 이렇게 푸는 걸 안해봤었다고????
# >> 내생각엔 O(N^2+N^2)까지는 괜찮은데 O(N^2* N) 이러면 시간초과나는 듯

import sys
input = sys.stdin.readline

N = int(input())
U = list(int(input()) for _ in range(N))
U.sort()

two = set()

for i in range(N):
	for j in range(i,N):
		two.add(U[i]+U[j])

for i in range(N-1,-1,-1):
	for l in range(N-2,-1,-1):
		if U[i]-U[l] in two:
			print(U[i])
			exit()


