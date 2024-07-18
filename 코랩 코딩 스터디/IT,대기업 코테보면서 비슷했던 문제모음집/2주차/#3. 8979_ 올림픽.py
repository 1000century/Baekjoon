# (세현)

N,K  = map(int,input().split())
medals = [list(map(int,input().split())) for _ in range(N)]
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 0
both = 1
before = [-1,-1,-1]
for i in range(0,N):
	if medals[i][1:] != before:
		rank = rank + both
		before = medals[i][1:]
		both = 1
	else:
		both = both + 1

	if medals[i][0] == K:
		print(rank)
		break
