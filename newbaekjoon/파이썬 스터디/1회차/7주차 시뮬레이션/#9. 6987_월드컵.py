from itertools import combinations, combinations_with_replacement,product, permutations

testcases = []
for i in range(4):
	temp = list(map(int,input().split()))
	result = [temp[0:3],temp[3:6],temp[6:9],temp[9:12],temp[12:15],temp[15:18]]
	result.sort()
	testcases.append(result)
ans = [0,0,0,0]
i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i2 = [1,2,3]
count = 0
for j in product(i2,repeat=15):
	temp = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	count = count + 1
	if j[0] == 1:
		temp[0][0] = temp[0][0] + 1
		temp[1][2] = temp[1][2] + 1
	elif j[0] == 2:
		temp[0][1] = temp[0][1] + 1
		temp[1][1] = temp[1][1] + 1
	elif j[0] == 3:
		temp[0][2] = temp[0][2] + 1
		temp[1][0] = temp[1][0] + 1

	if j[1] == 1:
		temp[0][0] = temp[0][0] + 1
		temp[2][2] = temp[2][2] + 1
	elif j[1] == 2:
		temp[0][1] = temp[0][1] + 1
		temp[2][1] = temp[2][1] + 1
	elif j[1] == 3:
		temp[0][2] = temp[0][2] + 1
		temp[2][0] = temp[2][0] + 1

	if j[2] == 1:
		temp[0][0] = temp[0][0] + 1
		temp[3][2] = temp[3][2] + 1
	elif j[2] == 2:
		temp[0][1] = temp[0][1] + 1
		temp[3][1] = temp[3][1] + 1
	elif j[2] == 3:
		temp[0][2] = temp[0][2] + 1
		temp[3][0] = temp[3][0] + 1

	if j[3] == 1:
		temp[0][0] = temp[0][0] + 1
		temp[4][2] = temp[4][2] + 1
	elif j[3] == 2:
		temp[0][1] = temp[0][1] + 1
		temp[4][1] = temp[4][1] + 1
	elif j[3] == 3:
		temp[0][2] = temp[0][2] + 1
		temp[4][0] = temp[4][0] + 1

	if j[4] == 1:
		temp[0][0] = temp[0][0] + 1
		temp[5][2] = temp[5][2] + 1
	elif j[4] == 2:
		temp[0][1] = temp[0][1] + 1
		temp[5][1] = temp[5][1] + 1
	elif j[4] == 3:
		temp[0][2] = temp[0][2] + 1
		temp[5][0] = temp[5][0] + 1


###################3

	if j[5] == 1:
		temp[1][0] = temp[1][0] + 1
		temp[2][2] = temp[2][2] + 1
	elif j[5] == 2:
		temp[1][1] = temp[1][1] + 1
		temp[2][1] = temp[2][1] + 1
	elif j[5] == 3:
		temp[1][2] = temp[1][2] + 1
		temp[2][0] = temp[2][0] + 1

	if j[6] == 1:
		temp[1][0] = temp[1][0] + 1
		temp[3][2] = temp[3][2] + 1
	elif j[6] == 2:
		temp[1][1] = temp[1][1] + 1
		temp[3][1] = temp[3][1] + 1
	elif j[6] == 3:
		temp[1][2] = temp[1][2] + 1
		temp[3][0] = temp[3][0] + 1

	if j[7] == 1:
		temp[1][0] = temp[1][0] + 1
		temp[4][2] = temp[4][2] + 1
	elif j[7] == 2:
		temp[1][1] = temp[1][1] + 1
		temp[4][1] = temp[4][1] + 1
	elif j[7] == 3:
		temp[1][2] = temp[1][2] + 1
		temp[4][0] = temp[4][0] + 1

	if j[8] == 1:
		temp[1][0] = temp[1][0] + 1
		temp[5][2] = temp[5][2] + 1
	elif j[8] == 2:
		temp[1][1] = temp[1][1] + 1
		temp[5][1] = temp[5][1] + 1
	elif j[8] == 3:
		temp[1][2] = temp[1][2] + 1
		temp[5][0] = temp[5][0] + 1


##############################



	if j[9] == 1:
		temp[2][0] = temp[2][0] + 1
		temp[3][2] = temp[3][2] + 1
	elif j[9] == 2:
		temp[2][1] = temp[2][1] + 1
		temp[3][1] = temp[3][1] + 1
	elif j[9] == 3:
		temp[2][2] = temp[2][2] + 1
		temp[3][0] = temp[3][0] + 1

	if j[10] == 1:
		temp[2][0] = temp[2][0] + 1
		temp[4][2] = temp[4][2] + 1
	elif j[10] == 2:
		temp[2][1] = temp[2][1] + 1
		temp[4][1] = temp[4][1] + 1
	elif j[10] == 3:
		temp[2][2] = temp[2][2] + 1
		temp[4][0] = temp[4][0] + 1

	if j[11] == 1:
		temp[2][0] = temp[2][0] + 1
		temp[5][2] = temp[5][2] + 1
	elif j[11] == 2:
		temp[2][1] = temp[2][1] + 1
		temp[5][1] = temp[5][1] + 1
	elif j[11] == 3:
		temp[2][2] = temp[2][2] + 1
		temp[5][0] = temp[5][0] + 1


#############################
	if j[12] == 1:
		temp[3][0] = temp[3][0] + 1
		temp[4][2] = temp[4][2] + 1
	elif j[12] == 2:
		temp[3][1] = temp[3][1] + 1
		temp[4][1] = temp[4][1] + 1
	elif j[12] == 3:
		temp[3][2] = temp[3][2] + 1
		temp[4][0] = temp[4][0] + 1

	if j[13] == 1:
		temp[3][0] = temp[3][0] + 1
		temp[5][2] = temp[5][2] + 1
	elif j[13] == 2:
		temp[3][1] = temp[3][1] + 1
		temp[5][1] = temp[5][1] + 1
	elif j[13] == 3:
		temp[3][2] = temp[3][2] + 1
		temp[5][0] = temp[5][0] + 1
#############################
	if j[14] == 1:
		temp[4][0] = temp[4][0] + 1
		temp[5][2] = temp[5][2] + 1
	elif j[14] == 2:
		temp[4][1] = temp[4][1] + 1
		temp[5][1] = temp[5][1] + 1
	elif j[14] == 3:
		temp[4][2] = temp[4][2] + 1
		temp[5][0] = temp[5][0] + 1
	
	if temp in testcases:
		ans[testcases.index(temp)] = 1


print(*ans)