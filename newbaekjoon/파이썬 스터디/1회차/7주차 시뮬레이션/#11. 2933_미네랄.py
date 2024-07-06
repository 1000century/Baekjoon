"""
# Part 1. 입력받기 + index 편하게 하기 위해서 cave는 거꾸로 입력받음.
	# Part 2. 파괴되는 점을 '.' 으로 바꾸기
	# Part 3a. h에 해당하는 row에 미네랄이 없는 경우 다음번 던지기로 넘어감.
	
	# Part 3b. h에 해당하는 row에 미네랄이 있어서 파괴되는 경우에는
 	 		파괴되는 점 기준으로 up,down,lt,rt 각각에 대해서 dfs탐색한다.
  
	 >> 염두에 두어야 할 점) 클러스터가 부서질 수는 있지만 떨어지는 경우는 오직 한 가지밖에 없음
	 >>> 즉, [(h+1,c),(h-1,c),(h,c+1),(h,c-1)]에서 하나라도 떨어지는 경우가 있다면, break하면 됨.
	 >>> (그나마 이 문제에서 착한 포인트) 

		# [단계 1] DFS 
		# [단계 2a] 만약 떨어질 수 있는 점이 없다면 다음 up,down,rt,lt로 넘어감.
		# [단계 2b] 떨어질 수도 있는 점이 존재한다면 column_check를 시행하여 두 가지 경우로 나눔.
			# A. 떨어지는 column이 없는 경우 > 다음 column으로 넘어감
			# B. 2b-1땅바닥과 맞닿아 있어서 못 떨어지는 경우
			# C. 2b-2 떨어질 수 있는 경우				
			
			*** 2b-1 과 2b-2 에서 벌어지는 일.
				2b-1) 다른 미네랄과 연결된 건 없지만 땅바닥에 굴러서 못 떨어지는 경우
				  >> 다음번 up,down,lt,rt로 넘어감.
				2b-2) 떨어질 수 있는 경우
				  >> cave의 구조가 바뀜.
					A. column에서 하강하는 미네랄이 없는 경우 > 다음 column으로 넘어감
					B. column에서 하강하는 미네랄이 있는 경우
					# >>> cave 에 new_col로 덮어씌움.

"""




# Part 1. 입력받기 + index 편하게 하기 위해서 cave는 거꾸로 입력받음.
R,C = map(int,input().split())
cave = [[] for _ in range(R)]
for i in range(R-1,-1,-1):
	cave[i] = input().replace(""," ").split()
N = int(input())
spear = list(map(int,input().split()))

for attempt in range(N):
#	print("_______attempt__",attempt)
#	for i in range(len(cave)-1,-1,-1):
#		print(cave[i])

	# Part 2. 파괴되는 점을 '.' 으로 바꾸기
	h = spear[attempt]-1
	destroyed = []

	if attempt%2 == 0:
		for c in range(C):
			if cave[h][c] == "x":
				destroyed = [h,c]
				cave[h][c] ='.'

				break
	else:
		for c in range(C-1,-1,-1):
			if cave[h][c] == "x":
				destroyed = [h,c]
				cave[h][c] ='.'
				break
	
	# Part 3a. h에 해당하는 row에 미네랄이 없는 경우 다음번 던지기로 넘어감.
	if destroyed==[]:
		continue
	
	# Part 3b. h에 해당하는 row에 미네랄이 있어서 파괴되는 경우.
 	# <<<파괴되는 점 기준으로 up,down,lt,rt 각각에 대해서 dfs탐색>>>
  
	# >> 염두에 두어야 할 점) 클러스터가 부서질 수는 있지만 떨어지는 경우는 오직 한 가지밖에 없음
	# >>> 즉, [(h+1,c),(h-1,c),(h,c+1),(h,c-1)]에서 하나라도 떨어지는 경우가 있다면, break하면 됨.
	# >>> (그나마 이 문제에서 착한 포인트) 

	for start_h,start_c in [(h+1,c),(h-1,c),(h,c+1),(h,c-1)]:
		# [단계 1] DFS 
		if not (0<=start_h<R and 0<=start_c<C):
			continue
		if cave[start_h][start_c] == '.':
			continue

		visited = [[0]*C for _ in range(R)]
		visited[start_h][start_c] = 1
		q = [(start_h,start_c)]
		iffall = [(start_h,start_c)]

		doesitfall = 1

		while q:
			ph,pc = q.pop()
			if ph == 0:
				doesitfall = 0
			for nh,nc in [(ph+1,pc),(ph-1,pc),(ph,pc+1),(ph,pc-1)]:
				if not (0<=nh<R and 0<=nc<C):
					continue
				if visited[nh][nc] == 1:
					continue
				if cave[nh][nc] == '.':
					visited[nh][nc] = 1
					continue
				q.append((nh,nc))
				visited[nh][nc] = 1
				iffall.append((nh,nc))

		# [단계 2a] 만약 떨어질 수 있는 점이 없다면 다음 up,down,rt,lt로 넘어감.
		if not doesitfall:
			continue

		# [단계 2b] 떨어질 수도 있는 점이 존재한다면
		# 두 가지 경우로 나뉨.
		# 2b-1) 다른 미네랄과 연결된 건 없지만 땅바닥에 굴러서 못 떨어지는 경우
		# 2b-2) 떨어질 수 있는 경우
		falling = [[] for _ in range(C)]
		for a,b in iffall:
			falling[b].append(a)
	#	print("falling",falling)

		depth = []
		
		# 떨어질 수 있는 점들을 column 단위로 check
		for col_chk in range(C):
			falling[col_chk].sort()

			# A. 떨어지는 column이 없는 경우 > 다음 column으로 넘어감
			if not falling[col_chk]:
				depth.append(1000) # 혹시나 오류생길까봐 넣은 값.
				continue
			
			# B. 2b-1땅바닥과 맞닿아 있어서 못 떨어지는 경우
			if min(falling[col_chk]) == 0: # 2b-1 (땅바닥과 닿아 있어서 못 떨어지게 됨)
				depth.append(0)
				break

			# C. 2b-2 떨어질 수 있는 경우
			dep_cnt = 0
			for i in range(min(falling[col_chk])-1,-1,-1):
				if cave[i][col_chk] == '.':
					dep_cnt = dep_cnt + 1
				else:
					break
			depth.append(dep_cnt)
		
		# [단계 2b-1] 다음번 up,down,lt,rt로 넘어감.
		if min(depth) == 0:
			continue

		# [단계 2b-2] cave의 구조가 바뀜.
		descent = min(depth)

		for col in range(C):

			# A. column에서 하강하는 미네랄이 없는 경우 > 다음 column으로 넘어감
			if not falling[col]:
				continue

			# B. column에서 하강하는 미네랄이 있는 경우
			# >>> cave 에 new_col로 덮어씌움.
			new_col = [0]*R

			for temp_h in falling[col]:
				new_col[temp_h-descent] = cave[temp_h][col]
				new_col[temp_h] = '.'

			for new_h in range(R):
				if new_col[new_h] != 0:
					cave[new_h][col] = new_col[new_h]


for i in reversed(cave):
	print(*i, sep='')