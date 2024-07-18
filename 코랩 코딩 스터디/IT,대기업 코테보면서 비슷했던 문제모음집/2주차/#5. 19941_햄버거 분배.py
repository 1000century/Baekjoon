# 백트래킹으로 푸니까 시간초과

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,K = map(int,input().split())

X = list(input().rstrip())
guys = []
ham = []
eaten = [0]*(N) # 햄버거랑 사람 섞여있지만 그냥 햄버거 먹은지만 확인할 리스트
for i in range(len(X)):
	if X[i] =="P":
		guys.append(int(i))
	else:
		ham.append(int(i))

def backtracking(g):
	if g == len(guys):
		return 0
	ans = 0
	gi = guys[g]
	for hi in ham:
		if abs(gi-hi)<=K:
			if eaten[hi] == 0:
				eaten[hi] = 1
				ans = max(ans,backtracking(g+1)+1)
				eaten[hi] = 0
		elif hi-gi>K:
			break
	ans = max(ans,backtracking(g+1))
	return ans
print(backtracking(0))