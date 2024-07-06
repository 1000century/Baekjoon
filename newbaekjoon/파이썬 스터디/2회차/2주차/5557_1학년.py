"""
1학년
https://www.acmicpc.net/problem/5557
"""
from itertools import product

N = int(input())
nums = list(map(int,input().split()))
cnt = 0

for x in product([1,2],repeat=N-2):
	x = list(x)
	cal = nums[0]
	goodnum = 1
	for idx in range(len(x)):
		i = x[idx]
		if i == 1:
			cal = cal + nums[idx+1]
		else:
			cal = cal - nums[idx+1]
		if cal >20:
			goodnum = 0
			break
		if cal < 0:
			goodnum =0
			break
	if goodnum == 1 and cal == nums[N-1]:
		cnt = cnt + 1
print(cnt)