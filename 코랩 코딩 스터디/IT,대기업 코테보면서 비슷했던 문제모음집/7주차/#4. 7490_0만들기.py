# (세현)

from itertools import product

def solution(N):
	for cals in product([' ','+','-'],repeat=N-1):
		temp = str(1)
		for i in range(1,N):
			temp = temp + cals[i-1]+str(i+1)
		temp2 = temp.replace(' ','')
		if eval(temp2) == 0:
			print(temp)

T = int(input())
for _ in range(T):
	N = int(input())
	solution(N)
	print()