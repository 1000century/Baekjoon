N = int(input())

attendance = {}
year = []
for _ in range(N):
	y, n = input().split()
	y = int(y)
	if y not in attendance:
		attendance[y] = [n]
		year.append(y)
	else:
		temp = attendance[y]
		temp.append(n)
		attendance[y] = temp
year.sort()
for y in year:
	x = attendance[y]
	for a in x:
		print(y, a)