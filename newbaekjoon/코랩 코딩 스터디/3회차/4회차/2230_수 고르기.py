
N,M = map(int,input().split())
A = list(int(input()) for _ in range(N))
A.sort()
ans = int(1e9)
st,en = 0,0
while en<N:
	if A[en]-A[st]>=M:
		ans = min(ans,A[en]-A[st])
		st = st -1
	else:
		en = en + 1
print(ans)