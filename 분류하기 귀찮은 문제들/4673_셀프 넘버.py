ans = []
for i in range(1,10000):
	sums= sum(int(digit) for digit in str(i))
	ans.append(i + sums)
	if i not in ans:
		print(i)

