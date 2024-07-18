N = int(input())
X = []
for _ in range(N):
	X.append(list(map(int,input().split())))

for i in range(N-2,-1,-1): # 5층까지 잇ㅋ다면 
	upperfloor = X[i+1]
	currentfloor = X[i]
	for j in range(len(currentfloor)):
		currentfloor[j] = max(currentfloor[j]+upperfloor[j],currentfloor[j]+upperfloor[j+1])

print(X[0][0])