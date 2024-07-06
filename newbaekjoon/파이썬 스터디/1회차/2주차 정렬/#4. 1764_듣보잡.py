"""
시간 오래 걸림 3696ms
"""

N,M = map(int,input().split())
X= []
for _ in range(N):
	X.append(input().rstrip())
for _ in range(M):
	X.append(input().rstrip())
X.sort()
Y = list(set(X))
print(N+M-len(Y))
before = ""
for i in range(len(X)-1):
	if X[i] == X[i+1] and X[i]!=before:
		print(X[i])
		