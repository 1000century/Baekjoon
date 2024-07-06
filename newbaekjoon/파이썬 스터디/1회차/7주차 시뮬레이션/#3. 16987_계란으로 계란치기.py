def dfs(index, eggs, weight, broken):
	if index == len(eggs):
		return broken
	# 현재 계란이 이미 깨진 경우
	if eggs[index] <= 0:
		return dfs(index + 1, eggs, weight, broken)
	# 이 계란을 다른 모든 계란과 부딪혀보기
	max_broken = broken
	for i in range(len(eggs)):
		if i != index and eggs[i] > 0:  # 다른 계란이고 깨지지 않았을 때만
			# 부딪히기
			eggs[index] -= weight[i]
			eggs[i] -= weight[index]
			# 다음 계란 처리
			next_broken = broken
			if eggs[index] <= 0:
				next_broken += 1
			if eggs[i] <= 0:
				next_broken += 1
			max_broken = max(max_broken, dfs(index + 1, eggs, weight, next_broken))
			# 원상태로 복구
			eggs[index] += weight[i]
			eggs[i] += weight[index]
	return max_broken

N = int(input())
eggs = []
weight = []
for i in range(N):
	a, b = map(int, input().split())
	eggs.append(a)
	weight.append(b)

result = dfs(0, eggs, weight, 0)
print(result)
