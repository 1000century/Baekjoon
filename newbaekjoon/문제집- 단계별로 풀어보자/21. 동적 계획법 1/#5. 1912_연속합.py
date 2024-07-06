# 이전 까지의 합이 현재 자신보다 작을 경우 무의미하다.

n = int(input().rstrip())
X = list(map(int,input().split()))
ans = X[0]
for i in range(1,n):
	X[i] = max(X[i],X[i-1]+X[i])
	ans = max(X[i],ans)
print(X)
print(ans)