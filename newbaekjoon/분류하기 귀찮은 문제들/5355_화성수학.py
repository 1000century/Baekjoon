"""
화성 수학
https://www.acmicpc.net/problem/5355
"""

T = int(input())
for _ in range(T):
	a = input().split()
	num = float(a[0])
	for i in range(1,len(a)):
		if a[i] == "@":
			num= num*3
		elif a[i] == "%":
			num = num+5
		else:
			num = num - 7
	print(f'{num:.2f}')
