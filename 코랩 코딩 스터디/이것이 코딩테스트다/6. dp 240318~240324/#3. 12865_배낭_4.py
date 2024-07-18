"""
for 물품 
	for 가방 무게

for 가방 무게
	for 물품

위에거보다 아래거가 메모리 더 많이 차지함
"""

# (세현)

N,K = map(int,input().split())

bagDP = [[0]*(K+1) for _ in range(N+1)]
ans = []
for i in range(1,N+1):
	weight, value = map(int,input().split())
	for j in range(0,K+1): # 가방무게가 j일때...
		if weight > j:
			bagDP[i][j] = bagDP[i-1][j]
		else:
			bagDP[i][j] = max(bagDP[i-1][j-weight]+value, bagDP[i-1][j])
	ans.append(bagDP[i][-1])
print(max(ans))