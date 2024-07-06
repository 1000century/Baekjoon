"""
24.03.11
35%에서 틀림 25%에서 틀림 47%에서 틀림 75프로에서 틀림

나타날 수 있는 오류들
1. 나누는 수가 0이 되는 오류
2. 가장 큰점(maxi)을 건너뛰게 되는 오류
"""

K,N = map(int,input().split())
X = []
for _ in range(K):
	X.append(int(input()))
maxi = max(X)


def binary(X, start, end):
	ans = 1
	while start+1<end: # start != end VS start +1 < end
		middle = (start + end) // 2
		count = 0
		for i in X:
			count = count + i // middle
		if count < N:
			start = start
			end = middle
		if count >= N:
			start = middle
			end = end
			ans = max(ans,middle)
	print(ans)

binary(X,0,maxi+1)