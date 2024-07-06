# (세현)

def test(Y=[],count=0):
	n, *X = map(int,input().split())
	for i in range(0,len(X)):
		Y.append(X[i])
		for j in range(0,i):
			if X[i] < Y[j]:
				count = count + i-j
				Y.insert(j,X[i])
				Y.pop()
				break
	print(n,count)

T = int(input())
for i in range(T):
	test([],0)