def solution(n):
	temp = []
	start = 1
	for i in range(n,0,-1):
		temp.append([i for i in range(start,start+i)])
		start = start + i
	print(*temp,sep='\n')

	answer = []
	for i in range(1,1+n):
		answer.append([0]*i)
	print(*answer,sep='\n')
	
	for i in range(len(temp)):
		print('---------------',i)
		print(temp[i])
		line = i//3
		if i % 3 == 0:
			for j in range(len(temp[i])):
				answer[line*2+j][line] = temp[i][j]
		elif i %3 == 1:
			for j in range(len(temp[i])):
				answer[-1-line][1+line+j] = temp[i][j]
		elif i %3 == 2:
			for j in range(len(temp[i])):
				answer[-2-line-j][-1-line] = temp[i][j]
		print(*answer,sep='\n')
	final = []
	for i in answer:
		for j in i:
			final.append(i)
	return final
solution(9)

