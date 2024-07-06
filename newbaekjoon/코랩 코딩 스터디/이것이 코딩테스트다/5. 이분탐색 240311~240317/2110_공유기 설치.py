"""
24.03.13 
pypy3기준 252ms (stdin안써도 통과)
python3 시간초과 (stdin쓰면 통과-456ms)

end를 가장 큰값으로 하면 오류 생김 + 반례)
2 2
0
1
"""
import sys
input = sys.stdin.readline
N, C = map(int,input().split())
X = []
for _ in range(N):
	X.append(int(input()))
X.sort()

def binary(X,C):
	begin = 1
	end = X[-1]-X[0]+1
	dist = (begin + end) // 2

	while begin < end:	
		num_C = C -1
		start = 0
		real_dist = []
		while start<len(X)-1:
			for t in range(start+1,N):
				if X[t]-X[start] >= dist:
					real_dist.append(X[t]-X[start])
#					print("dist는",dist,real_dist, "현재 t 통과.",t)
					start = t
					num_C = num_C - 1
					break
			if num_C == 0: # 거리가 남았다는 뜻 공유기 사이 거리 늘려도 됨
				begin = dist+1
				end = end
				dist = (begin + end) // 2
				ans = real_dist
#				print(dist,"공유기사이거리 늘려야","begin",begin,"end",end,'num_C',num_C)
				break

			if t == N-1:# 거리가 더 가버렸다. 뜻 공유기 사이 거리 줄여야 됨
				begin = begin
				end = dist
				dist = (begin + end) //2
#				print(dist,"공유기사이거리 줄여야","begin",begin,"end",end,'num_C',num_C)
				break
	print(min(ans))
				
binary(X,C)






