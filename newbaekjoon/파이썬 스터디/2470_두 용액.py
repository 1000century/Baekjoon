from bisect import bisect_right,bisect_left

N = int(input())
solu = list(map(int,input().split()))

solu.sort()
chk = 200000001

st = 0
en = len(solu)-1
ans = [solu[0],solu[-1]]
while st<en:
	te = sum(ans)
	if abs(te)<chk:
		ans = [solu[st],solu[en]]
		chk = abs(te)

	if te == 0:
		ans = [solu[st],solu[en]]
		break
	if te >0:
		en = en-1
	else:
		st = st + 1

print(*ans)


