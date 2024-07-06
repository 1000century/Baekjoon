N = int(input())
X = []
A = [0]*(N)

for _ in range(N):
	X.append(int(input()))

A[0] = [X[0]]

if N == 1:
	print(X[0])
	exit()
A[1] = [X[1],X[0]+X[1]] #앞에는 1칸연속, 뒤에는 2칸연속(즉 그 다음에는 두칸뛰어야함)

for i in range(2,N):
	onlyone = max(A[i-2]) + X[i]
	withtwo = A[i-1][0] + X[i]
	A[i] = [onlyone,withtwo]
print(max(A[-1]))