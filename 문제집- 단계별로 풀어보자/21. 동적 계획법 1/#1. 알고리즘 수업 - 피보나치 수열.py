N = int(input())

dp = N-2

A = [0,1]
for i in range(2,N+1):
	A.append(A[-1]+A[-2])

print(A[N],N-2)