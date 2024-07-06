# (세현)

# 시도1) 87% 시간초과
# 시도 2) stack

N = int(input())
tower = list(map(int,input().split()))

# Part 1. 왼쪽 관찰
stack = []
L_receive = [0]*N
cnt_L = [0]*N

for i in range(len(tower)):
	Ltemp = -10000000

	# 1. 자신보다 낮은 앞번호는 전부 제거
	while stack:
		if tower[stack[-1]] <=tower[i]:
			stack.pop()
		else:
			break
	cnt_L[i] = len(stack)

	# 2. 자신보다 낮은 앞번호가 존재한다면 가장 가까운 곳에서 수신
	if stack:
		Ltemp = stack[-1] + 1

	# 3. 자기 자신 추가
	stack.append(i)

	# 4. 수신하는 곳
	L_receive[i] = Ltemp


# Part 2. 오른쪽 관찰
stack = []
R_receive = [0]*N
cnt_R = [0]*N

for i in range(len(tower)-1,-1,-1):
	R_temp = -10000000

	# 1. 자신보다 낮은 뒷번호는 전부 제거
	while stack:
		if tower[stack[-1]] <=tower[i]:
			stack.pop()
		else:
			break
	cnt_R[i] = len(stack)

	# 2. 자신보다 낮은 뒷번호가 존재한다면 가장 가까운 곳에서 수신
	if stack:
		R_temp = stack[-1] + 1

	# 3. 자기 자신 추가
	stack.append(i)

	# 4. 수신하는 곳
	R_receive[i] = R_temp


# Part 3. 정답 출력
for i in range(N):
	if cnt_L[i] + cnt_R[i] == 0:
		print(0)
		continue

	if abs(L_receive[i]-i-1) > abs(R_receive[i]-i-1):
		receive = R_receive[i]
	else:
		receive = L_receive[i]

	print(cnt_L[i]+cnt_R[i],receive)
