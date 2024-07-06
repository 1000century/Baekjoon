# 24.03.28
# upperbound를 구해야 함

N = int(input())
A = list(map(int,input().split()))
M = int(input())

st = 0
en = max(A) # 처음에 M으로 해서 고침. M으로 하게 되면 expected<=M을 항상만족하기 때문에 st가 M+1까지 올라감.

while st <= en:
	mid = (st+en)//2

	expected = 0

	for i in A:
		if mid>i:
			expected = expected + i
		else:
			expected = expected + mid
	
	print(expected,st,en)
	if expected > M: # 예산이 너무 많이 드는 경우
		en = mid - 1
	else:
		st = mid + 1

print(st-1)