import sys
input = sys.stdin.readline

N = int(input())

dp= [[[0] * 10 for j in range(1 << N)] for i in range(N)] # M[artist][path(bin)][price]
# 10 >> 최대가격이 9이기 때문

arr = list(list(map(int,input().replace('', ' ').split())) for _ in range(N))

def dfs(artist,path,price):
	if dp[artist][path][price] != 0:
		return dp[artist][path][price]
	cnt = 1
	for nartist in range(1,N):
		if arr[artist][nartist] < price:
			continue
		if path & (1 << nartist) >0:
			continue
		cnt = max(cnt,1+dfs(nartist,path|(1<<nartist), arr[artist][nartist]))
	dp[artist][path][price] = cnt
	return cnt

print(dfs(0,1,0))