"""
시간초과
"""

N = int(input())
A = []
dic = {}
for _ in range(N):
	x = int(input())
	
	if not x == 0:
		if dic.get(x) == None:
			dic[x] = 0
			A.append(x)
			A.sort()
		else:
			dic[x] = dic[x] + 1
	else:
		if len(A) == 0:
			print(0)
		else:
			l = min(A)
			dic[l] == dic[l] - 1
			if dic[l] == 0:				
				A = A[1:]

			print(l)

