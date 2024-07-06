# (세현)

import sys
input = sys.stdin.readline

def solution(x):
	diff = x.count('X') - x.count('O')
	if diff != 0 and diff != 1:
		return 'invalid'

	ans = [x[0:3],x[3:6],x[6:],x[0]+x[4]+x[8], x[2]+x[4]+x[6],
		   x[0]+x[3]+x[6], x[1]+x[4]+x[7], x[2]+x[5]+x[8]]
	cnto = ans.count('OOO')
	cntx = ans.count('XXX')

	if cnto ==0 and cntx ==0:
		if '.' in x:
			return 'invalid'
		return 'valid'

	if diff == 1:
		if cnto == 0:
			return 'valid'
		return 'invalid'
	
	if diff == 0:
		if cntx == 0:
			return 'valid'
		return 'invalid'

while True:
	x = input().strip()
	if x == "end":
		break
	print(solution(x))