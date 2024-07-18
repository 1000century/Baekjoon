# (세현)
"""
24.03.15 16:41~
이분탐색 안된다.
"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))
collect.sort()

count = 0

if N ==1 or N ==2:
	print(0)
	exit()
for n in range(2,N):
	for search in range(n):
		ans = 0
#		print("n은", n,"search는",search)
		target = collect[n]
		need = target - collect[search]
		if need == collect[search]:
			if search-1>=0:
				if collect[search-1] == need:
					count = count + 1
					break # 찾았다. 완전탈출
				else:
					low = 0
					high = search - 1

			if search+1<= N-1:
				if collect[search+1] == need:
					count = count + 1
					break # 찾았다. 완전탈출
				else:
					low = search + 1
					high = N-1

			if search-1<0 and search+1>N-1:
				count = count + 0 # 변화없음
				break

		elif need < collect[search]:
			low = 0
			high = search-1
		elif need > collect[search]:
			low = search + 1
			high = n-1

		while low<=high: #닫힌구간
			mid = (low+high)//2
			if collect[mid] == need and search !=mid:
				count = count + 1
#				print(n,target,count,333)
#				print("도달했지롱.....n,target,need",n,target,need,"mid",mid)
				ans = 1
				break
			else:
				if collect[mid] > need:
					low = mid + 1
				else:
					high = mid -1
		if ans == 1:
			break
					
print(count)

		
	
	