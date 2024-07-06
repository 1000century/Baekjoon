M,N = map(int,input().split())

def space(X):
	A = sorted(list((x, i) for i, x in enumerate(X)))

	B = [0]*len(X)
	before = -1
	rank = -1
	temp = 1
	for x,idx in A:
		if x==before:
			temp = temp + 1
		else:
			rank = rank + temp
			temp = 1
		B[idx] = rank
		before = x
	return tuple(B)

from collections import defaultdict
q = defaultdict(int)
for i in range(M):
	X = space(list(map(int,input().split())))
	q[X] = q[X]+1

cnt = 0
for i,d in q.items():
	if d>1:	
		cnt = cnt+d*(d-1)//2
		
print(cnt)