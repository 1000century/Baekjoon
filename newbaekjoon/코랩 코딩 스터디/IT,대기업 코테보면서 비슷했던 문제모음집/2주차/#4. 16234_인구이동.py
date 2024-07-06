# 세현

from collections import deque

N,L,R = map(int,input().split())
population = [list(map(int,input().split())) for _ in range(N)]

def movement(DidTheyMoved = False):
	visited = [[0]*N for _ in range(N)]

	
	for h in range(N):
		for w in range(N):

			# Part 1. 그래프 탐색(BFS방식)
			if visited[h][w] == 0:
				union = deque([[h,w]])
				visited[h][w] = 1

				# ** 마지막에 population 추가해주기 위한 장치
				country = [(h,w)]
				population_num = population[h][w]

				while union:
					ph, pw = union.popleft()
					for nh,nw in [[ph+1,pw],[ph,pw+1],[ph-1,pw],[ph,pw-1]]:
						if 0<=nh<N and 0<=nw<N:
							if visited[nh][nw] ==0 and L<=abs(population[nh][nw]-population[ph][pw])<=R:
								union.append([nh,nw])
								visited[nh][nw] = 1

								# ** 마지막에 population 추가해주기 위한 장치
								country.append((nh,nw))
								population_num += population[nh][nw]
			
			# Part 2. 연합의 국가들에 평균인구 배분
			if len(country)>1:
				DidTheyMoved = True
				new_population_num = population_num // (len(country))
				for newh,neww in country:
					population[newh][neww] = new_population_num

	return DidTheyMoved

ans = 0
while True:
	if movement() == False:
		break
	ans = ans + 1
print(ans)