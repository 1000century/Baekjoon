# (세현)
"""
24.03.15 16:41~
이분탐색 안된다.

딕셔너리 + set 이용해서 풀기
67프로에서 오류

메모리초과

시간초과 엔딩 
"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))

count = 0

if N ==1 or N ==2:
	print(0)
	exit()
for n in range(0,N):
	target = collect[n]
	nagaja = 0

	hap = 0

	for start in range(N):
		end = start + 1
		if start == n:
			continue
		while end<N:
			if end == n or end ==start:
				end = end + 1
				continue
			hap = collect[start] + collect[end]
			if hap != target:
#				print("달라요",target,collect[start],collect[end])
				end = end + 1
			else:
				count = count + 1
#				print(count,target,collect[start],collect[end])
				nagaja = 1
				break
		if nagaja == 1:
			break




print(count)



