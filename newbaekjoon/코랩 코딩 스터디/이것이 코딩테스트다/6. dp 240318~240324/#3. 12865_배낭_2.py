# 0-1 배낭문제 (12865)
# 한 물건을 여러 개 담는 배낭문제 (12920)
# 물건을 원하는 분량만 쪼개서 담는 배낭문제 >> 그리디


N,K = map(int,input().split())
A = [[0,0]]
for _ in range(N):
	A.append(list(map(int,input().split())))

# bag에 관한 2차원 리스트로 만듦(무게 X 가치)
# 2차원 리스트 vs 1차원 리스트
bagDP = [[0]*(K+1) for _ in range(N+1)]


ans = []
for i in range(1,N+1): # 물품먼저 for문 돌림
	for j in range(1,K+1): # j는 배낭무게
		weight,value = A[i][0], A[i][1]
		if weight <= j: # 상품이 들어가는 경우 >> max(넣지말든가, 넣든가)
			bagDP[i][j] = max(bagDP[i-1][j], value + bagDP[i-1][j-weight])
		else: # 애초에 상품무게가 배낭무게보다 큰 경우 위에꺼 그대로 가져옴
			bagDP[i][j] = bagDP[i-1][j]
	ans.append(bagDP[i][-1])
print(max(ans))
