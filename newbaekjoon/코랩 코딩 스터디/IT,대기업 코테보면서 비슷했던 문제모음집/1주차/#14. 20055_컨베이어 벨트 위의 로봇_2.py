import sys
input = sys.stdin.readline

from collections import deque
N,K = map(int,input().split())
A = deque(list(map(int,input().split())))

robots = deque([])
for _ in range(2*N):
	robots.append(False)
lists = deque([])
up = 0%(2*N)
down = (N-1)%(2*N)
step = 1
while True:
	# 1. 벨트 회전
	rb = robots.pop()
	robots.appendleft(rb)
	ab = A.pop()
	A.appendleft(ab)

	for i in range(len(lists)): # 로봇이 들어온 순서대로 쌓인 로봇의 위치들 업데이트
		lists[i] =(lists[i] + 1)%(2*N)
	if len(lists) !=0 and lists[0] == down:
		lists.popleft()
	
	#2. 로봇 이동
	doesit = 0
	for i in range(len(lists)):
		now = lists[i]
		next = (lists[i] + 1)%(2*N)
		if A[next] ==0 or robots[next]==True: # 못 움직이는 경우
			continue
		robots[now] = False # 움직이는 경우
		robots[next] = True
		A[next] = A[next] - 1
		lists[i] = next
		if next == down:
			robots[next] = False
			doesit = 1
			continue
	if doesit == 1:
		lists.popleft()
	
	#3. 올린다.
	if robots[up] == False and A[up] >= 1:
		robots[up] = True
		lists.append(up)
		A[up] = A[up] - 1
	
	#4. 내구도 0인 칸의 개수가 K 이상이라면 과정 종료
	count = 0
	for i in A:
		if i == 0:
			count = count + 1
	if count>=K:
		print(step)
		break
	step = step + 1