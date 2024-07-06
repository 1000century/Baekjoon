# (세현)
# 이렇게 어이없게 풀리면 안 될 거 같고 다른 풀이가 있을 거 같음.

import sys
input = sys.stdin.readline

N,M,L,K = map(int,input().split())
stars = []
X,Y = set(),set()
for _ in range(K):
	x,y = map(int,input().split())
	X.add(x)
	Y.add(y)
	stars.append((x,y))

X,Y = list(X),list(Y)
X.sort()
Y.sort()

ans = K
for a in X:
	for b in Y:
		cnt = K
		for x,y in stars:
			if a<=x<=a+L and b<=y<=b+L:
				cnt = cnt - 1
		ans = min(ans,cnt)
print(ans)