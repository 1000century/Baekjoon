# (세현)

N = int(input())
X = []
for _ in range(N):
	X.extend(list(map(int,input().split())))
	X.sort(reverse=True)
	X = X[:N]
print(X[-1])
