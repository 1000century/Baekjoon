from itertools import combinations, product
import copy
a,b,c,d,e,f = [],[],[],[],[],[]
ans = []
for i in range(4):
	result = list(map(int,input().split()))
	a = result[0:3]
	b = result[3:6]
	c = result[6:9]
	d = result[9:12]
	e = result[12:15]
	f = result[15:18]

	if sum(a) != 5 or sum(b) != 5 or sum(c)!=5 or sum(c) != 5 or sum(d) != 5 or sum(e) != 5 or sum(f) != 5:
#		print("1번")
		ans.append(0)
		continue


	total_result = [0,0,0]
	for i in range(3):
		total_result[i] =a[i] + b[i] + c[i] + d[i] + e[i] + f[i]


	if total_result[0] != total_result[2]:
		ans.append(0)
#		print("2번")
		continue

	if sum(result) != 30:
		ans.append(0)
#		print("3번")
		continue

	cnt = 0
	if a[1] != 0:
		cnt = cnt + 1	
	if b[1] != 0:
		cnt = cnt + 1	
	if c[1] != 0:
		cnt = cnt + 1	
	if d[1] != 0:
		cnt = cnt + 1	
	if e[1] != 0:
		cnt = cnt + 1	
	if f[1] != 0:
		cnt = cnt + 1	
	if cnt == 1:
#		print("4번")
		ans.append(0)
		continue

	analysis = [a,b,c,d,e,f]
	analysis.sort(key=lambda x : x[0])
#	print(analysis)

	if analysis[0][1]==analysis[1][1]==analysis[2][1]==analysis[3][1]==analysis[4][1]==analysis[5][1]==5:
#		print("전부 무승부")
		ans.append(1)
		continue

	gonext = 0
	for i in range(6):
		if analysis[i][1] > total_result[1]-analysis[i][1]:
			gonext =1
			break
		if gonext == 1:
			ans.append(1)
			continue


	gonext = 0
	for i in range(6):
		if analysis[i][0] > total_result[2]-analysis[i][2]:
			gonext = 1
		if gonext == 1:
			ans.append(0)
			continue

	gonext = 0
	for i in range(6):
		if analysis[i][2] > total_result[0]-analysis[i][0]:
			gonext = 1
		if gonext == 1:
			ans.append(0)
			continue
			


	if analysis[0][0] == 0 and analysis[1][0] == 0:
		ans.append(0)
#		print("6번")
		continue
	
	if analysis[-1][0] ==5 and analysis[-2][0] == 5:
		ans.append(0)
#		print("7번")
		continue

#	print("____________________A______________--")
	teams = ["a","b",'c','d','e','f']
	temp_teams = [1,2,3,4,5]
	teamA = []
	for first in combinations(temp_teams,analysis[0][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[0][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[0][2]):
				teamA.append([first,second,third])
#	print("____________________B______________--")
	temp_teams = [0,2,3,4,5]
	teamB = []
	for first in combinations(temp_teams,analysis[1][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[1][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[1][2]):
				teamB.append([first,second,third])

#	print("____________________C______________--")
	temp_teams = [0,1,3,4,5]
	teamC = []
	for first in combinations(temp_teams,analysis[2][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[2][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[2][2]):
				teamC.append([first,second,third])


#	print("____________________D______________--")
	temp_teams = [0,1,2,4,5]
	teamD = []
	for first in combinations(temp_teams,analysis[3][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[3][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[3][2]):
				teamD.append([first,second,third])


#	print("____________________E______________--")
	temp_teams = [0,1,2,3,5]
	teamE = []
	for first in combinations(temp_teams,analysis[4][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[4][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[4][2]):
				teamE.append([first,second,third])

#	print("____________________F______________--")
	temp_teams = [0,1,2,3,4]
	teamF = []
	for first in combinations(temp_teams,analysis[5][0]):
		remaining = [x for x in temp_teams if x not in first]
		for second in combinations(remaining,analysis[5][1]):
			remaining_second = [x for x in remaining if x not in second]
			for third in combinations(remaining_second,analysis[5][2]):
				teamF.append([first,second,third])

	temp_analysis = copy.deepcopy(analysis)
	
	letsgo = 0

	for x in product(teamA,teamB,teamC,teamD,teamE,teamF):
		wrong = 0
		for k in range(6):
			if wrong == 1:
				break
			for w in x[k][0]:
				if k not in x[w][2]:
					wrong = 1
					break
		if wrong == 0:
			break

	if wrong == 0:
		ans.append(1)
	else:

		ans.append(0)
print(*ans)
