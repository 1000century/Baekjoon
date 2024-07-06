# (세현)

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
A = list(map(int,input().split()))
robots = [False]*(2*N)

step = 0
while True:
	step = step + 1
	
	# 1. 벨트 회전
	r1 = robots.pop()
	robots.insert(0,r1)
	a1 = A.pop()
	A.insert(0,a1)

	robots[N-1] = False

	# 2. 로봇 이동	
	if A[N-1]>0 and robots[N-2] == True:
		robots[N-2] = False
		A[N-1] = A[N-1] -1

	for i in range(N-3,-1,-1):
		if robots[i] == True and robots[i+1]==False and A[i+1]>0:
			robots[i],robots[i+1] = False,True # 움직이는 경우
			A[i+1] = A[i+1]-1

	#3. 올린다.
	if robots[0] == False and A[0] > 0:
		robots[0] = True
		A[0] = A[0] - 1
	
	#4. 내구도 0인 칸의 개수가 K 이상이라면 과정 종료
	if A.count(0) >=K:
		print(step)
		break
