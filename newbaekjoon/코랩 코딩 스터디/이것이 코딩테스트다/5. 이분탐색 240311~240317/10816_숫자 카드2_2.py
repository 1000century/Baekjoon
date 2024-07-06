# (세현)
"""
시간초과 계속 나오는 문제
24.03.15 10:48~
python3에서는 25%에서 시간초과
pypy3 에서는 63%에서 시간초과

N과 M이 모두 최대 500,000이므로 NM은 25*10**10입니다.
주어진 시간 제한 안에 할 수 있는 연산>>> 10**8번

upperbound lowerbound를 이용해서 풀어야 하는 문제
반례)
1
1
2
1 1
"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))
collect.sort()
# print(collect)

M = int(input())
isit = list(map(int,input().split()))


# LowerBound >> 여러개라면 가장 작은 값을 갖는 인덱스
# 같을 때 low는 고정하고 high값만 줄임

def isitin(collect, target):
	start_low = 0
	start_high = len(collect) # 반열린구간으로 정의

	low = start_low
	high = start_high
	while low<high:
		middle = (low + high) //2
		if target > collect[middle]:
			low = middle + 1
		else:
			high = middle
	begin = low
	## 이 말은 endpoint에서는 low 가 high보다 커진 경우임

	low = start_low
	high = start_high
	while low < high:
		middle = (low + high) // 2
		if target < collect[middle]:
			high = middle
		else:
			low = middle + 1
	end = low
	temp = end - begin

	return temp
for i in isit:
	answer = isitin(collect,i)
	print(answer,end=" ")