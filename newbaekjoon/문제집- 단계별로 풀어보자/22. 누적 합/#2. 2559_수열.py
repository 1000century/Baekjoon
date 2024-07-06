N,K = map(int,input().split())
A = list(map(int,input().split()))

AA=[0]
for i in A:
	AA.append(AA[-1]+i)

## AA의 원소 개수 N + 1 - K 에다가 0추가해서 N + 2 - K
ans = -201000000
for i in range(K,N+1):
	hap = AA[i]-AA[i-K]
	ans = max(ans,hap)
print(ans)