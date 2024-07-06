N = int(input())
U = []
for i in range(N):
	U.append(int(input()))
U.sort()

X = set()
for i in range(N):
	for j in range(N):
		X.add(U[i]+U[j])
def check():
	for i in range(N-1,-1,-1):
		for j in range(i+1):
			if U[i]-U[j] in X:
				return U[i]
print(check())
