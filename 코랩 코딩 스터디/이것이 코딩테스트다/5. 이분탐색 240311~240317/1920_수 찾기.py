# (세현)
"""
24.03.15 10:41~
이것도 마찬가지로 list(set())쓰는 게 더 빠름

# start와 end 범위를 단힌구간으로 하기 (0~N-1 로 하기 vs 1~N 으로 하기)
					vs 반열림구간으로 하기 (0~N vs 1~N+1)
# 종료조건을 start<=end vs start<end-1 vs start != end

일단은 닫힌구간으로 하는 것이 익숙..
"""
N = int(input())
collect = list(map(int,input().split()))
collect.sort()

M = int(input())
isit = list(map(int,input().split()))

def whether(collect, element):
	st = 0
	end = len(collect)
	ans = 0
	while st<end:
		middle = (st + end) //2
		if collect[middle] < element:
			st = middle + 1
		elif collect[middle] > element:
			end = middle
		else:
			ans = 1
			break
	return ans

for i in isit:
	answer = whether(collect,i)
	print(answer)
	
	
