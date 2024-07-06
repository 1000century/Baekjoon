"""
아이디어:
5*5 조합에서 7개를 선택하는 모든 조합의 경우의 수를 저장
각 경우의 수 기준으로 
		1. 7명이 서로 연결되어 있는지
		2. 이다솜파가 4명이상 있는지
		"?
를 확인하여 모두 만족할 때만 정답 카운트
"""

from itertools import combinations

count = 0
cluster = [list(input().strip()) for _ in range(5)]

# 1. 연결성 확인
def connection(seats):
	seats_set = set(seats)
	start = seats[0]
	visited = set()
	stack = [start]
	while stack:
		x, y = stack.pop()
		if (x, y) in visited:
			continue
		visited.add((x, y))
		for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if (nx, ny) in seats_set and (nx, ny) not in visited:
				stack.append((nx, ny))
	
	# 7명 확인
	if len(visited) == 7:
		return 1
	else:
		return 0

# Part 1. 7명을 뽑는 모든 경우의 수 구하기
seven_students_list = []
for i in range(5):
	for j in range(5):
		seven_students_list.append((i,j))


# Part 2. 그 경우의 수가 조건을 만족하는지 확인하기
for seven_students in combinations(seven_students_list, 7):
	# dasom >> 이다솜파 4명인지
	# connection >> 연결되어 있는지
	dasom = 0
	for x,y in seven_students:
		if cluster[x][y] == 'S':
			dasom = dasom + 1
	if dasom >= 4 and connection(seven_students):
		count += 1

print(count)
