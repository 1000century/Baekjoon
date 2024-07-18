"""
소음
https://www.acmicpc.net/problem/2935
"""

A = len(input())-1
x = input()
B = len(input())-1

if x == "*":
	print(1,end='')
	p = '0'*(A+B)
	print(p)
elif x == '+':
	if A == B:
		print(2,end='')
		p = '0'*(A)
		print(p)
	else:
		k = [0]*(max(A,B)+1)
		k[-1] = 1
		k[min(A,B)] = 1
		print(*reversed(k),sep='')


