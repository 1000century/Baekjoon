N,K = map(int,input().split())
A = list(map(int,input().split()))

from collections import deque
robots = []
for i in range(2*N):
	robots.append(False)
lists = deque([])

up = (-1)%(2*N)
down = (N-2)%(2*N)
step = 1
while True:
	# 1. 벨트 회전
	rightend = robots.pop()
	robots = [rightend]+robots

	temp = []
	for i in range(len(lists)): # 로봇이 들어온 순서대로 쌓인 로봇의 위치들 업데이트
		moved =(lists[i] + 1)%(2&N)
		if moved == down:
			robots[down] = False
			continue
		temp.append(moved)
	print(A,robots,"단계",step, "1",lists,temp)
	lists = temp[:]
	
	#2. 로봇 이동
	temp2 = []
	for i in range(len(lists)):
		now = lists[i]
		next = (lists[i] + 1)%(2*N)
		if A[next] ==0 or robots[next]==True: # 못 움직이는 경우
			temp2.append(now)
			continue
		robots[now] = False # 움직이는 경우
		robots[next] = True
		A[next] = A[next] - 1
		lists[i] = next
		if next == down:
			robots[next] = False
			continue
		temp2.append(next)
	lists = temp2[:]
	print(A,robots,"단계",step, "2")
	
	#3. 올린다.
	if robots[up] == False and A[up] >= 1:
		robots[up] = True
		lists.append(up)
		A[up] = A[up] - 1
	print(A,robots,"단계",step, "3","3단계에 올린 로봇을 포함한", lists)
	
	#4. 내구도 0인 칸의 개수가 K 이상이라면 과정 종료
	count = 0
	print(A,robots,"단계",step)
	for i in A:
		if i == 0:
			count = count + 1
	if count>=K:
		print(step)
		break
	step = step + 1
	print("_____________________단계끝_____________")




