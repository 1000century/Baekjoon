N = int(input())

def test(N):
	count = N
	
	if N <= 9:
		return count

	for i in range(10,N+1):
		X = list(map(int,str(i)))
		diff = X[0]-X[1]
		for j in range(1,len(X)-1):
			d = X[j] - X[j+1]
			if d != diff:
				count = count -1
				break
	return count
	
print(test(N))