"""
24.03.17 17:38 ~ 18:49
"""
T = int(input())

def booster_vel(X,Y,V): # 부스터 속력(Z)은 Y가 최대, X 는 트랙길이
	highest = max(V[:-1])
	me = V[-1]

	# case 1. 부스터 없이 내가 제일 빠른 경우
	if me > highest:
		return 0

#	# case 2. 경주가 1초 이내로 끝나는 경우 ( V는 모두 정수이다.)
#	if X <= highest:
#		if highest >= Y:
#			return -1
#		elif highest <Y:
#			return highest + 1 # 딱 상대보다 1만큼만 큰 속도의 부스터가 필요
	
	# case 3. 일반적인 경우 > 이분탐색
	st = me
	en = Y
	first_time = X / highest

	while st <=en:
		mid = (st + en) // 2
		dist = mid + me * (first_time -1)*(first_time-1 >0) ### 불리안연산으로 case2,3를 합침
		if dist >X:
			en = mid - 1
		else:
			st = mid + 1

	if st > Y:
		return -1
	else:
		return st

for _ in range(T):
	N,X,Y = map(int,input().split()) # Z는 반드시 Y 이하, 내 자동차 번호는 N, X 는 트랙길이
	V = list(map(int,input().split())) # 처음 1초간 Z m/s 그 이후에는 V m/s

	print(booster_vel(X,Y,V))
