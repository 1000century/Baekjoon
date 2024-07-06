T = int(input())
for _ in range(T):
	n = int(input())
	X = [[0]*(n+1)]
	for a in range(2):
		temp = [0]
		temp.extend(list(map(int,input().split())))
		X.append(temp)
#	print(*X,sep='\n')

	dp = [[0,0] for _ in range(n+2)]
	
	ans = max(X[1])
	for i in range(2,n+2): # N = 1일때 생각하기 귀찮으니 두 칸의 여유분을 만듦
		a = dp[i-1][0] # 바로왼쪽 위
		b = dp[i-1][1] # 바로왼쪽 아래
		c = dp[i-2][0] # 두칸왼쪽 위
		d = dp[i-2][1] # 두칸왼쪽 아래

		valueU = X[1][i-1]
		valueD = X[2][i-1]

		dp[i][0] = max(a, max(b,c)+valueU) # 이게 그냥   max(b,d) + valueU ??
		dp[i][1] = max(b, max(a,d)+valueD) # 이것도 그냥 max(a,c) + valueD ??
	ans = max(ans,max(dp[i]))
	print(ans)
#	print(*dp,sep='\n')
