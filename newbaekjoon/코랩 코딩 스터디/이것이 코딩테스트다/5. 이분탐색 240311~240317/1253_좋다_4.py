# (세현)
"""
24.03.15 16:41~ 03.17 01:33

시도 1) 딕셔너리 + set 이용해서 풀기 67프로에서 오류
시도 2) 메모리초과
시도 3) 시간초과 엔딩 >> 함수 def을 따로 빼니까 일단 시간초과를 어느 정도 해결함
시도 4) 89%에서 틀렸습니다. >> 반례 5) 가 문제였음
시도 5) 투포인터 + 이분탐색 >>> python3 + stdin >> 5204ms

반례1) 정답: 4
5   
-2 0 -1 -1 -2

반례2) 정답: 4
5
0 0 0 0 1

반례3) 정답: 4 
4
0 0 0 0

반례4) 정답 : 1
3
-5 -2 -3

반례 5) 정답 : 0
3
0 0 1
"""
import sys
N = int(sys.stdin.readline())
collect = list(map(int,sys.stdin.readline().split()))
collect.sort()

def counter(collect,n):
	target = collect[n]

	# 개념) 투 포인터 + 이분탐색 섞임
	for search in range(N):

		# part 1. target의 인덱스와 구해야하는 두 수의 인덱스, 즉 세 개의 수의 인덱스는 서로 달라야 함
		if search == n:
			continue
		need = target - collect[search]

		# part 2. 구해야 하는 두 수의 값이 같을 때, 인덱스가 다른 경우에만 return 1
		if need == collect[search]:
			if search-1>=0 and collect[search-1] == need and search-1 != n:
				return 1
			elif search+1<= N-1 and collect[search+1] == need and search+1 !=n:
				return 1
			else:
				continue

		# part 3. 이분 탐색 위끝, 아래끝 설정
		if need < collect[search]:
			low = 0
			high = search-1
		elif need > collect[search]:
			low = search + 1
			high = N-1
		
		# part 4. 이분탐색 실행 
		while low<=high: #닫힌구간
			mid = (low+high)//2
			if collect[mid] == need and search !=mid and mid != n: # 세 수의 인덱스가 다르다는 조건도 넣음
				return 1
			else:
				if collect[mid] > need:
					high = mid -1
				else:
					low = mid + 1
	return 0

count = 0
for n in range(N):
	count = count + counter(collect,n)
					
print(count)