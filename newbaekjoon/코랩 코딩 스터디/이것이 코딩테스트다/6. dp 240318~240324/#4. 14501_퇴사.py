## 실패..

N = int(input()) # N일 일하고 퇴사

X = [[0,0]]
for _ in range(N):
	X.append(list(map(int,input().split())))

workDP = [[0]*(N+1) for _ in range(N+1)]
ans = 0
for i in range(1,N+1): #일을 받은 날
	T, P = X[i][0], X[i][1] # T는 걸리는 시간, P는 수익
	for j in range(1,N+1): # j일날 퇴사한다면,,
		if j<T+i-1: # 일 할 수 없다면,,,
			workDP[i][j] = workDP[i][j-1]
			#비교함... 일하지 않거나 or
		else: # 일 할 수 있다면 효용비교해야함.
			workDP[i][j] = max(workDP[i-1][j-T]+P,workDP[i-1][j])
	ans = max(ans,workDP[i][-1])
print(workDP)
print(ans)
