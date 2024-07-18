def solution(s):
	elements = s[2:-2].split('},{')
	sets = []
	for element in elements:
		num_set = set(map(int, element.split(',')))
		sets.append(num_set)
	sets.sort(key=len)

	answer = []
	temp = set()
	for i in sets:
		for j in i:
			if j not in temp:
				answer.append(j)
				temp.add(j)

	return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")