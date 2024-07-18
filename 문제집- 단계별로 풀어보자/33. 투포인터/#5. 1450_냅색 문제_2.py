# 시도 1) 2차원 리스트 dp >> 메모리초과
# 시도 2) 1차원 리스트 2개 dp >> 메모리초과

N, C = map(int,input().split())
things = list(map(int,input().split()))

things.sort()

dp = [0]*(N)
bag_now = [1]*(C+1)

for i in range(N):
	w = things[i]
	bag_before = bag_now
	bag_now = [1]*(C+1)
	for j in range(1,C+1):
		if w > j:
			bag_now[j] = bag_before[j] # 넣지 않겠다.
			continue
		bag_now[j] = bag_before[j-w] + bag_before[j]

print(bag_now[-1])
#print(*bag,sep='\n')
