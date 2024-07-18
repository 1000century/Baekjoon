INF = int(1e9)
N,M = map(int,input().split())

fuel = [[INF]+ list(map(int,input().split())) + [INF] for _ in range(N)]

dp1 =[[INF]+ [0]*M+[INF] for _ in range(N)]
dp2 =[[INF]+ [0]*M+[INF] for _ in range(N)]
dp3 =[[INF]+ [0]*M+[INF] for _ in range(N)]

dp1[0] = fuel[0] # 하강
dp2[0] = fuel[0] # 왼쪽아래방향
dp3[0] = fuel[0] # 오른쪽아래방향

for i in range(1,N): # 첫 행은 하드코딩으로 처리해줬으므로 1부터 시작
	for j in range(1,M+1): # 0번 인덱스, M+1번 인덱스는 패딩해준 것임으로 제외
		dp1[i][j] = fuel[i][j] + min(dp2[i-1][j],dp3[i-1][j])
		dp2[i][j] = fuel[i][j] + min(dp1[i-1][j+1],dp3[i-1][j+1])
		dp3[i][j] = fuel[i][j] + min(dp1[i-1][j-1],dp2[i-1][j-1])
print(min(min(dp1[-1]),min(dp2[-1]),min(dp3[-1])))

"""
print("_--------------수직하강----------")
print(*dp1,sep='\n')

print("_--------왼쪽 아래로-----------")
print(*dp2,sep='\n')

print("_----------오른쪽 아래로----------------")
print(*dp3,sep='\n')

"""