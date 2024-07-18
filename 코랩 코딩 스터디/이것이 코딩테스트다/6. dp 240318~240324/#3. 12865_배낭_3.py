# (세현)
N,K = map(int,input().split())
X = [[0,0]]
for _ in range(N):
	X.append(list(map(int,input().split())))
X.sort()
#print(X)

bagDP = [[0]*(N+1) for _ in range(K+1)]

for i in range(0,K+1): # 가방무게가 i일때...
	for j in range(1,N+1):
		weight, value = X[j][0], X[j][1]
		if weight > i:
			bagDP[i][j:N+1] = [bagDP[i][j-1]]*(N+1-j)
			break
		else:
			bagDP[i][j] = max(bagDP[i-weight][j-1]+value, bagDP[i][j-1])
#print(bagDP)
print(max(bagDP[-1]))