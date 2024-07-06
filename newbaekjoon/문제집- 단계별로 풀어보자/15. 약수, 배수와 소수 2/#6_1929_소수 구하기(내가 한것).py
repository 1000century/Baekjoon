import sys
M,N = map(int,sys.stdin.readline().split())

a = int((N**2) ** 0.5)+1
A = []
if M == 1:
	A.append(1)
for x in range(2,a+1):
	end = (a // x) + 1
	for i in range(x,end+1):
		if x*i <M:
			pass
		elif x* i <= N:
			A.append(x*i)
		else:
			break
A = list(set(A))
A.sort(reverse=True)
#count = 0
for num in range(M,N+1):
	if len(A) == 0:
		for num in range(num,N+1):
			sys.stdout.write(str(num) + '\n')
		break
		
	elif num == A[-1]:
		A.pop()
	else:
		sys.stdout.write(str(num)+'\n')
		
#		count = count + 1
#print(count)