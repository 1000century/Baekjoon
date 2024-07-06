# 시도1) 87% 시간초과

N = int(input())
X = [0] + list(map(int,input().split()))

Xrt = [0]*(N+1)
Xlt = [0]*(N+1)
Xn = [[] for _ in range(N+1)]

for i in range(1,N+1):
	for j in range(i,0,-1):
		if X[i] < X[j]:
			Xlt[i] = Xlt[j] + 1
			Xn[i].append(j)
			break
for i in range(N,0,-1):
	for j in range(i,N+1):
		if X[i] < X[j]:
			Xrt[i] = Xrt[j]+1
			Xn[i].append(j)
			break


for i in range(1,N+1):
	if not Xn[i]:
		print(0)
	else:
		if len(Xn[i]) == 1:
			print(Xrt[i]+Xlt[i],Xn[i][0])
		else:
			ansX = Xrt[i]+Xlt[i]
			if abs(Xn[i][0]-i) > abs(Xn[i][1]-i):
				print(Xrt[i]+Xlt[i],Xn[i][1])
			else:
				print(Xrt[i]+Xlt[i],Xn[i][0])

							
