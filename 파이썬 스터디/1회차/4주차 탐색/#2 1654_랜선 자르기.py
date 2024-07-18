"""
24.03.28
처음에 개수에 초점을 맞춰서 lowerbound문제인가 헀는데
개수는 길이를 나눈 값이고, 결국 search하는 랜선기준으로는
최대가 나와야하니까 upperbound를 구하고 upperbound - 1 해줘야함.
"""

# Lower bound
# 정렬 된 배열(nums)에서 찾고자 하는 값(target) 이상이 처음 나타나는 위치

# Upper bound
# 정렬 된 배열(nums)에서 찾고자 하는 값(target)보다 큰 값이 처음 나타나는 위치

"""
나타날 수 있는 오류들
1. 나누는 수가 0이 되는 오류 >> 시작점을 0부터가 아닌 1로 바꿔주면 됨
2. 가장 큰점(maxi)을 건너뛰게 되는 오류   >>> 끝점을 maxi+1로 바꿔주면 됨 
										>>> 아니면 닫힌구간처리해주면 됨
"""


K,N = map(int,input().split())
cord = [int(input()) for _ in range(K)]

st = 1
en = cord[-1]

while st<=en:
	mid = (st+en)//2

	count = 0
	for c in cord:
		count = count + c//mid
	
	if count >= N: # 너무 많이 만들었음 
		st = mid + 1

	else:
		en = mid - 1
print(st-1)