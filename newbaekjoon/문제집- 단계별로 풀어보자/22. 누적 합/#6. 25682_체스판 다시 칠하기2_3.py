"""
492ms

"""

import sys

N,M,K = map(int,sys.stdin.readline().split())

temp = [[0]*(M+K+1) for _ in range(N+K+1)]
ans = 400000001
Y = [0]*(M+K+1)
for i in range(1,N+1):
	X = [0]*(K+1)+list(sys.stdin.readline().rstrip())
	add_value = 0
	for j in range(1,M+1):
		if ((i-j) % 2 == 1 or X[K+j] == "W") and ((i-j) % 2 == 0 or X[K+j] == "B"):
			add_value = add_value + 1
		X[j+K] = add_value + Y[j+K]
		temp[i+K][j+K] = X[j+K] - X[j]
	Y = X

#print("CHESS")
#print(*chess,sep='\n')

#print("TEMP")
#print(*temp,sep='\n')

for i in range(K,N+1):
	for j in range(K,M+1):
		rough = temp[i+K][j+K] - temp[i][j+K]
		ans = min(ans, rough, K*K-rough)
print(ans)
