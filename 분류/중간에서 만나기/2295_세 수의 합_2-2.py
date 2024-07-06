# 시도 여러번 후) 질문게시판을 찾아보다가 해보니 pypy로만 통과
# 시도 2) 이렇게 푸는 걸 안해봤었다고????
# >> 내생각엔 O(N^2+N^2)까지는 괜찮은데 O(N^2* N) 이러면 시간초과나는 듯
# 다 해보고 앞에꺼 왜 틀렸는지 다시 풀어봄.. > 우선 시간초과 난 이유는 위에 적은거랑 같음
# 하다가 틀릴 리가 없는데  틀렸지? >> U.sort() 안해줬으니까..

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
U = list(int(input()) for _ in range(N))
U.sort()

sumU = defaultdict(list)

for i in range(N):
	for j in range(i,N):
		val = U[i] + U[j]
		sumU[val]=1

for target in reversed(U):
	for i in U:
		if sumU[target-i]==1:
			print(target)
			exit()