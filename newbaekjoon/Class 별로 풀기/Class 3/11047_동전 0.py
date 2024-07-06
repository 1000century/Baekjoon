N,K = map(int,input().split())
A = []
for _ in range(N):
	x = int(input())
	if x<=K:
		A.append(x)

count = 0
for i in range(len(A)-1,-1,-1):
	coin = A[i]
	count = count + K//coin
	K = K%coin
print(count)