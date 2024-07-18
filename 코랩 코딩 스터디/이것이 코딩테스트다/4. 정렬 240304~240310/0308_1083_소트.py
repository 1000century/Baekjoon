import time
"""
3/7 11:58~

아이디어 N개의 숫자라면
for ㅑ in range(N):
	i번 인덱스로 옮길 수 있을만큼 옮김
		>>>> while문 사용

왠지 모르겠지만 value error가 뜸
"""
N = int(input())
X = list(map(int,input().split()))
S = int(input())

while len(X) != 0:
	while max(X[0:S+1]) == X[0]:
		print(X.pop(0), end=" ")
		N = N-1
		print("//",N,S)
		if N == S: # X[0:S+1] 인덱스가 안채워지는 경우 break
			break

	count = 0
	while S != 0:
		M = max(X)
		ind = X.index(M)
		while S < ind-count:
			M = max(X[0:ind-count])
			ind = X.index(M)
			count = count + 1
			

		if S>=ind:
			print(X.pop(ind), end = " ")
			N = N-1
			S = S-ind
			count = 0
			

	
for i in X:
	print(i, end =" ")