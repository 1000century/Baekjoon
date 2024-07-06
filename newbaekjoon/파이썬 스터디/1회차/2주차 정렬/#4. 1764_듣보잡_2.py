"""
시간 오래 걸림 3696ms

그래서 딕셔너리 쓰는 거 사용
근데 그래서 이 문제의 의의가 뭐지?
"""

N,M = map(int,input().split())
X= {}
Y = []
for _ in range(N+M):
	a = input()
	if X.get(a) == None:
		X[a] = 0
	else:
		Y.append(a)

print(len(Y))
Y.sort()
for i in Y:
	print(i)


