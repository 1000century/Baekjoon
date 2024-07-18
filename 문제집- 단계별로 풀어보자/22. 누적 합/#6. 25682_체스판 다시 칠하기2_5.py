"""
나의 최단기록
python3 4792ms
pypy3 444ms
"""

import sys
data = sys.stdin.read()
lines = data.split('\n')

N,M,K = map(int,lines[0].split())

chess = [[0]*(M+K+1) for _ in range(N+K+1)]
ans = 400000001
Y = [0]*(M+K+1)
for i in range(1,N+1):
	X = [0]*(K+1)+list(lines[i])
	add_value = 0
	for j in range(1,M+1):
		if ((i-j) % 2 == 1 or X[K+j] == "W") and ((i-j) % 2 == 0 or X[K+j] == "B"):
			add_value = add_value + 1
		X[j+K] = add_value + Y[j+K]
		chess[i+K][j+K] = X[j+K] - X[j]
	Y = X

#print("CHESS")
#print(*chess,sep='\n')

#print("chess")
#print(*chess,sep='\n')

for i in range(K,N+1):
	for j in range(K,M+1):
		rough = chess[i+K][j+K] - chess[i][j+K]
		ans = min(ans, rough, K*K-rough)
print(ans)
