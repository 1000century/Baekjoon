# 아래서부터 탐색해야 하므로 입력받은 puyo를 거꾸로 뒤집어 주었음.
puyo = [[] for _ in range(12)]
for i in range(11,-1,-1):
	puyo[i] = input().replace(''," ").split()

def graph_search_for_color(x,y,color):
	# 전역함수 >> stage, visited
	q = [[x,y]]
	temp_change = [(x,y)]
	while q:
		px,py = q.pop()
		for nx,ny in [(px+1,py),(px-1,py),(px,py-1),(px,py+1)]:
			if not (0<=nx<12 and 0<=ny<6): # 범위 제한 확인
				continue
			if visited[nx][ny] == 1: 	   # 방문확인
				continue
			if puyo[nx][ny] == color:
				visited[nx][ny] = 1
				q.append([nx,ny])
				temp_change.append((nx,ny))

	if len(temp_change)>=4:
		stage.extend(temp_change)



chain = 0 # 몇 연쇄?

while True:

	# Part 1. 그래프 탐색(BFS탐색)
	visited = [[0]*6 for _ in range(12)]
	stage = []

	for x in range(12):
		if puyo[x] == ['.', '.', '.', '.', '.', '.']:
			break
		for y in range(6):
			if visited[x][y] == 1:
				continue
			visited[x][y] = 1

			if puyo[x][y] in "RGBPY":
				graph_search_for_color(x,y,puyo[x][y])

	# Part 2a. 이번 stage에서 연쇄가 일어나는 경우
	if stage:
		# 1. stage에서 모은 바꿔야 하는 칸을 각 column별로 구분
		breakdown = [[],[],[],[],[],[]]
		for a,b in stage:
			breakdown[b].append(a)
		
		# 2. puyo의 각 column이 new_col로 새롭게 바뀌게 됨. 
		for i in range(6):
			if not breakdown[i]:
				continue

			new_col = []
			for j in range(12):
				if j not in breakdown[i]:
					new_col.append(puyo[j][i])
			while len(new_col) < 12:
				new_col.append('.')
			
			for nj in range(12):
				puyo[nj][i] = new_col[nj]

		# 3. 연쇄 cycle이 1씩 추가됨.
		chain = chain + 1
				
	# Part 2b. 이번 stage에서 연쇄가 일어나지 않으면 종료
	else:
		break
print(chain)


