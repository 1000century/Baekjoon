# (세현)

N = int(input())

col = []
for _ in range(N):
	L,H = map(int,input().split())
	col.append((L,H))
col.sort(key=lambda x:x[0])

lt = 0
height_a = 0
squ_lt = 0
for l,h in col:
	if h >= height_a:
		squ_lt = squ_lt + height_a*(l-lt)
		height_a = h
		lt = l

rt = 1001
height_b = 0
squ_rt = 0
col.sort(reverse = True)
for l,h in col:
	if lt >l: # 오른쪽에서 탐색할 때는 이 부분만 다름
		break
	if h >=height_b:
		squ_rt = squ_rt + height_b*(rt-l)
		rt = l
		height_b = h
print(squ_lt+squ_rt+height_a)