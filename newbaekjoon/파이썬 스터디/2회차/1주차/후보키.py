from itertools import combinations
def solution(relation):
	answer = 0
	used = set()
	for k in range(1,1+len(relation)):
		for comb in combinations(list(i for i in range(len(relation[0]))),k):
			comb = sorted(list(comb))
			sets = set()
			for j in range(len(relation)):
				pora = []
				for idx in comb:
					pora.append(str(relation[j][idx]))
				sets.add(tuple(pora))
			if len(sets) == len(relation):
				used.add(tuple(comb))
	print(used)
	used = list(used)
	used.sort(key = lambda x:len(x))
	temp_used = used.copy()
	for i in range(len(used)):
		for j in range(i+1,len(used)):
			key1 = set(used[i])
			key2 = set(used[j])
			if key1.issubset(key2):
				try:
					temp_used.remove(key2)
				except:
					continue

	return len(temp_used)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	
print("정답",solution(relation))
print("정답",solution([["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]))

print("정답",solution([["100","ryan","music","2"],
		["200","apeach","math","2"],
		["300","tube","computer","3"],
		["400","con","computer","4"],
		["500","muzi","music","3"],
		["600","apeach","music","2"]]))
print("정답",solution([["a", "1", "aaa", "c", "ng"], ["a", "2", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]))

print('정답',solution( [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))