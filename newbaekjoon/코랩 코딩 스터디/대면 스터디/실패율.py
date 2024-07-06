# (세현)
def solution(N, stages):
	step = {i:0 for i in range(1,N+2)} # 각 stage에 머무르고 있는 유저 수
	reach = {i:0 for i in range(1,N+2)} # 각 stage까지 도달한 유저 수
	hard = {i:0 for i in range(1,N+2)} # 각 stage의 난이도

	for i in stages:
		step[i] = step[i] + 1
	reach[N+1] = step[N+1]

	for i in range(N,0,-1):
		reach[i] = reach[i+1] + step[i]
		if reach[i] ==0: # 도달한 유저수가 0인 경우, 난이도는 0
			continue
		hard[i] = step[i] / reach[i]

	ans = []
	for i in range(1,N+1):
		ans.append([hard[i],i])
	ans.sort(key = lambda x: -x[0])
	answer = []
	for i in ans:
		answer.append(i[1])
	
	return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))