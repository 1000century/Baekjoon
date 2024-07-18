

def rotttery():
	kX = list(map(int,input().split()))
	if kX ==[0]:
		return 1
	k, X = kX[0], kX[1:]

	def combination(index,arr):
		if len(arr) == 6:
			print(*arr)
			return
		for i in range(index,k):
			arr.append(X[i])
			combination(i+1,arr)
			arr.pop()
	combination(0,[])

while True:
	a = rotttery()
	if a == 1:
		break
	print()