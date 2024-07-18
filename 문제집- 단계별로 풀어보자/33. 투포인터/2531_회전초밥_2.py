# 시도 1) 쿠폰집합, 시작번호별로 먹을 수 있는 접시개수 dp, 먹었는지 체크하는 리스트 다 넣음
#		  처음에 시간 1000ms 나오길래 뭐지 했는데 나중에 알고보니까 stdin 썼을 때 제일 빠름
# 시도 2) 투포인터 적용해서 풀었음 >> start, end

N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
# N: 접시 수
# d: 초밥종류개수
# k: 연속해서 먹는 접시 수
# c: 쿠폰번호

s = 0
e = k
eat = [0]*(d+1)
eat_set = set()
for i in range(s,e):
	new = sushi[i%N]
	eat[new] = eat[new]+1
	eat_set.add(new)

eat[c] = eat[c] + 1
eat_set.add(c)

ans = len(eat_set)
while s < N:
	front = sushi[s%N]
	back = sushi[e%N]

	eat[front] = eat[front]-1
	if eat[front] == 0:
		eat_set.remove(front)

	eat[back] = eat[back] + 1
	eat_set.add(back)
	
	s = s + 1
	e = e + 1
	ans = max(ans,len(eat_set))
print(ans)


	

