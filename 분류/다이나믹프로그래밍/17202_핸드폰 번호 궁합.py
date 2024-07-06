"""
이게 왜 dp문제?
"""

N1 = list(input())
N2 = list(input())
X = []
for i in range(len(N1)):
	X.append(int(N1[i]))
	X.append(int(N2[i]))
while len(X) >2:
	temp = []
	for i in range(len(X)-1):
		temp.append((X[i]+X[i+1])%10)
	X = temp[:]
print(*temp,sep="")