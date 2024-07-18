T = int(input())

for k in range(T):
	N = int(input())
	cloth = {}
	number = []
	for _ in range(N):
		name,category = input().split()
		if cloth.get(category) == None:
			cloth[category] = 1
			number.append(category)
		else:
			cloth[category] = cloth[category]+1

	ans = 1
	for i in number:
		ans = ans * (cloth[i] + 1)
	print(ans-1)

