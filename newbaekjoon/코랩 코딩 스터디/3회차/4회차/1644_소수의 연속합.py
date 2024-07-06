N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

i,j = 0,0
new = []
while i<N and j<M:
	if A[i]<B[j]:
		new.append(A[i])
		i = i + 1
	else:
		new.append(B[j])
		j= j + 1

if j == M:
	new = new + A[i:]
elif i == N:
	new = new + B[j:]
print(*new)