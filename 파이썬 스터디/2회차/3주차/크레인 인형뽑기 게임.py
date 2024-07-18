"""
크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""

def solution(board, moves):
	stack = []
	answer = 0
	N = len(board)
	for i in moves:
		i = i -1
		for j in range(N):
			if board[j][i] !=0:
				stack.append(board[j][i])
				board[j][i] = 0
				break
		while len(stack)>=2 and stack[-1] == stack[-2]:
			stack.pop()
			stack.pop()
			answer = answer + 2

	return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]	))