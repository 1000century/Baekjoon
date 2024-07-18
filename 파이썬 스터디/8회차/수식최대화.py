import re

def plus(temp):
	while '+' in temp:
		idx = temp.index('+')
		temp[idx-1] = temp[idx-1] + temp[idx+1]
		del temp[idx], temp[idx]
	return temp

def minus(temp):
	while '-' in temp:
		idx = temp.index('-')
		temp[idx-1] = temp[idx-1] - temp[idx+1]
		del temp[idx], temp[idx]
	return temp

def gop(temp):
	while '*' in temp:
		idx = temp.index('*')
		temp[idx-1] = temp[idx-1] * temp[idx+1]
		del temp[idx], temp[idx]
	return temp


def solution(expression):
	new = []
	ans = 0
	temp = ''
	for i in expression:
		if i in ['-','+','*']:
			new.extend([int(temp),i])
			temp = ''
		else:
			temp = temp + i
	new.append(int(temp))
	
	ans = max(ans, abs(gop(minus(plus(new[:])))[0]))
	ans = max(ans, abs(minus(gop(plus(new[:])))[0]))
	ans = max(ans, abs(gop(plus(minus(new[:])))[0]))
	ans = max(ans, abs(plus(gop(minus(new[:])))[0]))
	ans = max(ans, abs(plus(minus(gop(new[:])))[0]))
	ans = max(ans, abs(minus(plus(gop(new[:])))[0]))

	return ans

