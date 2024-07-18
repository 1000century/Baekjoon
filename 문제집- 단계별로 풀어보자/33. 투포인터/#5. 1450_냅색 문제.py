# 시도 1) 2차원 리스트 dp >> 메모리초과

N, C = map(int,input().split())
things = list(map(int,input().split()))

things.sort()

dp = [0]*(N)
bag = [[1]*(C+1) for _ in range(N)]

for i in range(N):
	w = things[i]
	for j in range(1,C+1):
		if w > j:
			bag[i][j] = bag[i-1][j] # 넣지 않겠다.
			continue
		bag[i][j] = bag[i-1][j-w] + bag[i-1][j]

print(bag[-1][-1])
#print(*bag,sep='\n')
