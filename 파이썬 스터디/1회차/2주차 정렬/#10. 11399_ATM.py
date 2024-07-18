N = int(input())
X = list(map(int,input().split()))

X.sort()
time = 0
for i in range(N):
	time = time + X[i] *(N-i)
print(time)
