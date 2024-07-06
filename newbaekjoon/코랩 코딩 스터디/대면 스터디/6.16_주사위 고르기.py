from itertools import combinations,product
from collections import defaultdict
def solution(dice):
	ans = 0
	for arr in combinations([i for i in range(len(dice))],len(dice)//2):
		di = defaultdict(int)
		db = defaultdict(int)
		a = []
		temp = []
		b = []
		for i in range(len(dice)):
			if i in arr:
				a.append(dice[i])
				temp.append(i)
			else:
				b.append(dice[i])
		
		for x in product(*a):
			di[sum(x)] = di[sum(x)]+1
		for x in product(*b):
			db[sum(x)] = db[sum(x)]+1
		win = 0
		xxxx = 0
		for ka,va in di.items():
			xxxx = xxxx+va
			for kb,vb in db.items():
				if ka>kb:
					win = win + va*vb			
		if win>=ans:
			ans = win
			answer = temp
	real = [i+1 for i in answer]
	return real
dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]	
print(solution(dice))