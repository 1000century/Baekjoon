# (세현)

N = int(input())
A = [0] + list(map(int,input().split()))
B = A[:]
for i in range(1,len(A)):
	for j in range(i):
		if A[j]<A[i]:
			B[i] = max(B[i], B[j]+A[i])

print(max(B))