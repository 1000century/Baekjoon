"""
35%에서 틀림
25%에서 틀림
binary(X,1,maxi) 0>1로 바꾸니까 47%에서 틀림
binary(X,1,maxi+1) maxi > maxi+1 로 바꾸니까 75프로에서 틀림

그냥 print(max(ans)) 를 아래처럼 바꾸니까 맞음 
	if len(ans) !=0:
		print(max(ans))
	else:
		print(1)

나타날 수 있는 오류들
1. 나누는 수가 0이 되는 오류 >> 시작점을 0부터가 아닌 1로 바꿔주면 됨
2. 가장 큰점(maxi)을 건너뛰게 되는 오류 >> 끝점을 maxi+1로 바꿔주면 됨
"""
import sys
K,N = map(int,sys.stdin.readline().split())
X = []
for _ in range(K):
	X.append(int(sys.stdin.readline()))
maxi = sum(X)//K


def binary(X, start, end):
	while start<=end: # start != end VS start +1 < end
		middle = (start + end) // 2
		count = sum([x//middle for x in X])
		if count < N:
			start = start
			end = middle-1
		if count >= N:
			start = middle+1
			end = end
			ans = middle
	print(ans)

binary(X,1,maxi+1)