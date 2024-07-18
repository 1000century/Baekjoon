
# 1) 백트래킹으로 푸니까 시간초과
# 2) dfs로 해도 시간초과
# 3) 아이디어 찾아봄 
# >> 사람의 위치에서 양쪽으로 k의 범위에서 가장 왼쪽에 있는 햄버거 고르기
N,K = map(int,input().split())
X = ["padding"]*K+list(input()) +["padding"]*K
count = 0
for i in range(K,N+K):
	if X[i] != "P":
		continue
	for j in range(i-K,i+K+1):
		if X[j] == "H":
			count = count + 1
			X[j] = "changed"
			break
print(count)