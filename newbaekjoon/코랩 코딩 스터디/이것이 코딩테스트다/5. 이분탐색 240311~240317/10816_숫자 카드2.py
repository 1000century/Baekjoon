# (세현)
"""
시간초과 계속 나오는 문제
24.03.15 10:48~
python3에서는 25%에서 시간초과
pypy3 에서는 63%에서 시간초과

N과 M이 모두 최대 500,000이므로 NM은 25*10**10입니다.
주어진 시간 제한 안에 할 수 있는 연산>>> 10**8번

"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))
collect.sort()

M = int(input())
isit = list(map(int,input().split()))

def isitin(collect, element):
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
			x = middle
			while x>=1: # before
				before = x -1
				if collect[before] == element:
					ans = ans + 1
					x = x -1
				else:
					break
			x = middle
			while x<=(len(collect)-2): #after
				after = x + 1
				if collect[after] == element:
					ans = ans + 1
					x = x + 1
				else:
					break

			break
	return ans

for i in isit:
	answer = isitin(collect,i)
	print(answer,end=" ")