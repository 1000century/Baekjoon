# 시도 1) 쿠폰집합, 시작번호별로 먹을 수 있는 접시개수 dp, 먹었는지 체크하는 리스트 다 넣음
#		  처음에 시간 1000ms 나오길래 뭐지 했는데 나중에 알고보니까 stdin 썼을 때 제일 빠름
# 시도 2) 투포인터 적용해서 풀었음 >> start, end
# 시도 3) 투포인터 그대로하긴 했지만 defaultdict사용함

from collections import defaultdict
import sys
input = sys.stdin.readline
N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
# N: 접시 수
# d: 초밥종류개수
# k: 연속해서 먹는 접시 수
# c: 쿠폰번호

s = 0
e = k
eat = defaultdict(int)
for i in range(s,e):
	new = sushi[i]
	eat[new] = eat[new] + 1

eat[c] = eat[c] + 1

ans = len(eat)
while s < N:
	front = sushi[s]
	back = sushi[e%N]

	eat[front] = eat[front]-1
	if eat[front] == 0:
		eat.pop(front)

	eat[back] = eat[back] + 1
	
	s = s + 1
	e = e + 1
	ans = max(ans,len(eat))
print(ans)