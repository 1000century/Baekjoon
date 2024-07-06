# 0-1 배낭문제 (12865)
# 한 물건을 여러 개 담는 배낭문제 (12920)
# 물건을 원하는 분량만 쪼개서 담는 배낭문제 >> 그리디
N, K = map(int,input().split())

goods = []
goods.append([0,0])
for _ in range(N):
	W,V = map(int,input().split())
	goods.append([W,V])
goods.sort()
knapsack = [[0]*(K+1) for _ in range(N+1)]
print(goods)
print(knapsack)

for i in range(1,N+1): # N은 물품 개수
	for j in range(1,K+1): # K는 가방무게
		weight = goods[i][0]
		value = goods[i][1]

		if j < weight: # 못들어가는 경우는 이전꺼 복붙
			knapsack[i][j] = knapsack[i-1][j]
		else:
			knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack)
