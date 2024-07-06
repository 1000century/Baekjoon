#1) 부분합 리스트 구하고 투포인터
#2) 그냥 바로 투포인터
# vs for문 + 투포인터

N,S = map(int,input().split())
numbers= list(map(int,input().split()))

lt, rt  = 0,0
numsum = 0
ans = int(1e9)

while True:
	if numsum >=S:
		ans = min(ans,rt-lt)
		numsum = numsum -numbers[lt]
		lt = lt + 1
	elif rt == N: # 이 부분이 조금 불편
		break
	else:
		numsum = numsum +numbers[rt]
		rt = rt + 1


if ans == int(1e9):
	print(0)
else:
	print(ans)