from collections import deque,defaultdict

def solution(board):
	N = len(board)
	visited = set()
	cost = defaultdict(lambda: int(1e9))
	
	q = deque([(0,0,0,0)])
	# (x,y,방향,cost)
	visited.add((0,0,0))
	cost[(0,0,0)] = 0
	
	while q:
		x,y,d,cnt = q.popleft()
		directions = [(x+1,y,d),(x,y+1,d),(x-1,y,d),(x,y-1,d)]
		
		if d == 0:  # 가로
			if x > 0 and board[x-1][y] == 0 and board[x-1][y+1] == 0:
				directions.append((x-1,y,1))
				directions.append((x-1,y+1,1))
			if x < N-1 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
				directions.append((x,y,1))
				directions.append((x,y+1,1))
		elif d == 1:  # 세로
			if y > 0 and board[x][y-1] == 0 and board[x+1][y-1] == 0:
				directions.append((x,y-1,0))
				directions.append((x+1,y-1,0))
			if y < N-1 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
				directions.append((x,y,0))
				directions.append((x+1,y,0))
		
		for nx,ny,nd in directions:
			if nd == 0:
				if not (0 <= nx < N and 0 <= ny < N-1):
					continue
				if board[nx][ny] + board[nx][ny+1] != 0:
					continue
			else:
				if not (0 <= nx < N-1 and 0 <= ny < N):
					continue
				if board[nx][ny] + board[nx+1][ny] != 0:
					continue
			
			if cost[(nx,ny,nd)] > cnt + 1:
				cost[(nx,ny,nd)] = cnt + 1
				q.append((nx,ny,nd,cnt + 1))
	
	answer = int(1e9)
	if cost[(N-1,N-2,0)] != int(1e9):
		answer = min(answer,cost[(N-1,N-2,0)])
	if cost[(N-2,N-1,1)] != int(1e9):
		answer = min(answer,cost[(N-2,N-1,1)])
	
	return answer
