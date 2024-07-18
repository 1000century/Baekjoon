from collections import defaultdict

from collections import defaultdict,deque
N, P, Q = map(int, input().split())
P, Q = min(P, Q), max(P, Q)

q = set()
q.add(N)

i = N
while i != 0:
	q.add(i)
	i = i // P
i = N
while i != 0:
	q.add(i)
	i = i // Q

q = list(q)
q.sort()

A = defaultdict(int)
A[0] = 1
for i in q:
	if i ==0:
		continue
	if (A.get(i//Q) != None and A.get(i//P) != None):
		A[i] = A[i//P] + A[i//Q]
	else:
		if A.get(i//Q) == None:
			x = i//Q
			temp = []
			while x != 0:
				temp.append(x)
				x = x//Q
			temp.sort()
			for c in temp:
				A[c]  = A[c//P] + A[c//Q]
		else:
			x = i//P
			temp = []
			while x != 0:
				temp.append(x)
				x = x//P
			temp.sort()
			for c in temp:
				A[c]  = A[c//P] + A[c//Q]


		A[i] = A[i//P] + A[i//Q]
print(A)
print(A[N])



