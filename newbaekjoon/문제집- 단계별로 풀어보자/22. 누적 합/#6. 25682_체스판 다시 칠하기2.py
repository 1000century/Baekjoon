
"""
pypy3 650ms >> 572ms 까지는 줄임..
"""
import sys

N,M,K = map(int,sys.stdin.readline().split())

chess = [[0]*(M+K+1) for _ in range(K+1)]
temp = [[0]*(M+K+1) for _ in range(N+K+1)]
ans = 400000001
for i in range(1,N+1):
	add_value = 0
	X = [0]*(K+1)+list(sys.stdin.readline().rstrip())
	for j in range(1,M+1):
		if ((i-j) % 2 == 1 or X[j+K] == "W") and ((i-j) % 2 == 0 or X[j+K] == "B"):
			add_value = add_value + 1
		X[j+K] = add_value + chess[i+K-1][j+K]
		temp[K+i][K+j] = temp[K+i-1][K+j]+ (X[j+K] - X[j]) - (chess[i-1][j+K]-chess[i-1][j])
#		temp[K+i][K+j] = temp[K][K+j] + (X[j+K] - X[j]) - (chess[i-1][j+K]-chess[i-1][j])
	print(X)
	
	chess.append(X)
print("chess")
print(*chess,sep='\n')
print("temp")
print(*temp,sep='\n')
for i in range(1,N-K+2):
	for j in range(1,M-K+2):
		rough = temp[-i][-j]
		ans = min(ans, rough, K*K-rough)
print(ans)


