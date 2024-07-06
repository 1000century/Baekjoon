N = int(input())
signal = input()

length = N//5
row = [[] for _ in range(length)]

for i in range(N):
	now = i % length
	if signal[i] == "#":
		row[now].append(1)
	else:
		row[now].append(0)

num_codes,now = [],[]
for i in range(length):
	if row[i] == [0,0,0,0,0]:
		if now:
			num_codes.append(now)
			now = []
	else:
		now.append(row[i])
if now:
	num_codes.append(now)

result = ''
for each_num in num_codes:
	if each_num == [[1,1,1,1,1]]:
		result = result+'1'
	elif each_num == [[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1]]:
		result = result +'0'
	elif each_num == [[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1]]:
		result = result +'2'
	elif each_num == [[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]:
		result = result +'3'
	elif each_num == [[1,1,1,0,0],[0,0,1,0,0],[1,1,1,1,1]]:
		result = result + '4'
	elif each_num == [[1,1,1,0,1],[1,0,1,0,1],[1,0,1,1,1]]:
		result = result + '5'
	elif each_num == [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,1,1]]:
		result = result + '6'
	elif each_num == [[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]]:
		result = result + '7'
	elif each_num == [[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]:
		result = result + '8'
	elif each_num == [[1,1,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]:
		result = result + '9'

print(result)



