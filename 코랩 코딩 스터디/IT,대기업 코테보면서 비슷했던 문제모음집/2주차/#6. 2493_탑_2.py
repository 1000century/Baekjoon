# (세현)

N = int(input())
tower = list(map(int,input().split()))
stack = []

for i in range(len(tower)):
	receiver = 0 # 수신기는 0으로 초기화

	# 1. 스택에서 자신보다 낮은 앞번호는 전부 제거
	while stack:
		if tower[stack[-1]] <=tower[i]:
			stack.pop()
		else:
			break

	# 2. 자신보다 높으면서 가장 가까운 위치에 있는 수신기 탐색
	if stack:
		receiver = stack[-1] + 1

	# 3. 스택에 자기 자신 추가
	stack.append(i)

	# 4. 수신기 출력
	print(receiver)