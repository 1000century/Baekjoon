import re
def solution(dartResult):
	answer = 0

	game = []
	temp = []
	for i in range(len(dartResult)):
		if dartResult[i] in ['0','1','2','3','4','5','6','7','8','9']:
			if i == 0:
				temp = [dartResult[i]]
				continue
			if temp and temp[-1] in  ['0','1','2','3','4','5','6','7','8','9']:
				temp = ['10']
			else:
				game.append(temp)
				temp = [dartResult[i]]
		else:
			temp.append(dartResult[i])
	game.append(temp)

	ans = []
	for i in game:
		if i[1] =="S":
			gop = 1
		elif i[1] == "D":
			gop = 2
		elif i[1] == "T":
			gop = 3
		
		temp = int(i[0])**gop
		if len(i)==3 and i[2] == '*':
			if len(ans) != 0:
				ans[-1] = ans[-1]*2
			ans.append(2*temp)
		elif len(i)==3 and i[2] == '#':
			ans.append(-temp)
		else:
			ans.append(temp)
	answer = sum(ans)	
	return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
