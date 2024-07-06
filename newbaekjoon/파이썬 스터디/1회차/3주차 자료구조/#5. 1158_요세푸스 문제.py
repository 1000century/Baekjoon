N, K = map(int,input().split())

X = []
for i in range(1,N+1):
	X.append(i)

ans = []
a = 1
tempn = N
tempk = K
for _ in range(N):
	a = (a + K-1) % (tempn)
	tempn = tempn - 1
	print(a)
	ans.append(X[a-1])
	del X[a-1]
print(ans)