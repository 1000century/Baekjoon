# (세현)
"""
24.03.15 10:17~10:21

return > break > break 부분을 깔끔하게 할 필요가 있을듯
이분탐색 > 1740ms
있는지없는지 list 만들어서 하는 거 > 860ms
"""
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
			break
	return ans

for i in isit:
	answer = isitin(collect,i)
	print(answer,end=" ")
	
	
