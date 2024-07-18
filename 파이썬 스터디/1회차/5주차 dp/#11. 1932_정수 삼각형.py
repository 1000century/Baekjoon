n = int(input())
X = [[0,0]] + [[0]+ list(map(int,input().split()))+[0] for _ in range(n)]
dp = [[0]*(i+1) for i in range(1,n+2)]
# print(X)
for i in range(1,n+1):
	for j in range(1,i+1):
		dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + X[i][j]

# print(*dp, sep='\n')
print(max(dp[-1]))


"""
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
"""