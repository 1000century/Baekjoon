na,nb = map(int,input().split())
A = set(list(map(int,input().split())))

for i in list(map(int,input().split())):
	if i in A:
		A.remove(i)
if len(A) == 0:
	print(0)
else:
	print(len(A))
	print(*sorted(list(A)))