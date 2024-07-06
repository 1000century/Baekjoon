N,M = map(int,input().split())
chess = [[0]*(M+1)]
for i in range(1,N+1):
	X = [0]+list(input())
	for j in range(1,M+1):
		if (i+j) % 2 == 0:
			if X[j] == "B":
				X[j] = 0 + X[j-1] + chess[i-1][j]- chess[i-1][j-1]
			else:
				X[j] = 1 + X[j-1] + chess[i-1][j]- chess[i-1][j-1]
		else:
			if X[j] == "W":
				X[j] = 0 + X[j-1] + chess[i-1][j]- chess[i-1][j-1]
			else:
				X[j] = 1 + X[j-1] + chess[i-1][j]- chess[i-1][j-1]
	chess.append(X)
#print(*chess,sep='\n')

temp = [[0]*(M+1) for _ in range(N+1)]

temp = [[0]*(M+2-8) for _ in range(N+2-8)]

ans = 400000001
for i in range(1,N-6):
	for j in range(1,M-6):
		rough = chess[i+8-1][j+8-1] - chess[i-1][j+8-1] - chess[i+8-1][j-1] + chess[i-1][j-1]
		temp[i][j] = rough
		ans = min(ans, rough, 8*8-rough)
#print(*temp,sep='\n')
print(ans)


