N = int(input().strip())
solu = list(map(int,input().strip().split()))
solu.sort()

st = 0
en = N-1

chk = 2000000001
while st<en:
	te = solu[st]+solu[en]
	if te == 0:
		ans = [solu[st],solu[en]]
		break
	if abs(te)<chk:
		ans = [solu[st],solu[en]]
		chk = abs(te)

	if solu[st]+solu[en] >0:
		en = en-1
	else:
		st = st + 1

print(*ans)