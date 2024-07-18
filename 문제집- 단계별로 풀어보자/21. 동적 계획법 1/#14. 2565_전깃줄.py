import sys

N = int(sys.stdin.readline())
A =[]
for _ in range(N):
	X = list(map(int,sys.stdin.readline().split()))
	A.append(X)

A.sort()
#print(A)

dp = [1]*N
for i in range(1,N):
	line = A[i]
	for j in range(0,i):
		nextline = A[j]

		if line[1]>nextline[1]:
			dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))
