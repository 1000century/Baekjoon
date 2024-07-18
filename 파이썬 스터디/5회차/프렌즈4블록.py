def solution(m, n, board):
	answer = 0
	turn = 1
	temp = [[0]*n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			temp[i][j] = board[i][j]
	board = temp[:]

	while turn == 1:
		turn = 0
		broken = [[0]*n for _ in range(m)]
		for i in range(m-1):
			for j in range(n-1):
				if board[i][j] == 0:
					continue
				if (board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]):
					broken[i][j],broken[i+1][j],broken[i][j+1],broken[i+1][j+1]=1,1,1,1
					turn = 1

		result = [[0]*n for _ in range(m)]

		for j in range(n):
			h = m-1
			for i in range(m-1,-1,-1):
				if not broken[i][j]:
					result[h][j]= board[i][j]
					h = h-1
				else:
					answer = answer + 1
		board = result[:]
	return answer
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])
print("testcase")
solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])