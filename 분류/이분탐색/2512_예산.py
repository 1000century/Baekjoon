N = int(input())
X = list(map(int,input().split()))
M = int(input())
st = 1 # 닫힌 구간
en = max(X) # 닫힌 구간

if sum(X) <= M:
	ans = max(X)
else:
	while st<=en:
		mid = (st+en) // 2
		maxi = M
		for i in range(1,N+1):
			maxi = maxi - min(mid,X[i-1])
		if maxi <0:
			en = mid - 1
		else:
			st = mid + 1
			ans = mid

print(ans)

