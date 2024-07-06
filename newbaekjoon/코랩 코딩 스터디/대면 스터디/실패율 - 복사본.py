def solution(N, stages):
	answer = []
	stage = dict()
	for i in range(1,501):
		stage[i] = 0

	for s in stages:
		if s<=N:
			stage[s]+=1

	challenge = []
	ppl = len(stages)
	for k,v in stage.items():
		if k <= N and ppl!=0:
			challenge.append([k,v/ppl])
			ppl-=v
	challenge.sort(key=lambda x: (-x[1]))
	answer = [c[0] for c in challenge]

	return answer
print(solution(2,[1,1,1,1]))
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))