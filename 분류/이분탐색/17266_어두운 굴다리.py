"""
24.03.17 16:52~17:08

이거 분류가 왜 이분탐색?
"""
N = int(input()) #굴다리 길이
M = int(input()) # 가로등 개수
X = list(map(int,input().split()))

d = 0
for i in range(M-1):
	d = max(X[i+1]-X[i],d)

height = d // 2 + (d % 2 > 0) # 이거 좀 외우자

if X[0] != 0:
	height = max(height,X[0])
if X[-1] != N:
	height = max(height,N-X[-1])
print(height)

