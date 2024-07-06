def solution(msg):
	dict ={}
	for idx,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
		dict[c] = idx+1

	idx = 0
	answer = []
	cnt = 27
	temp = ''
	"kakao"
	while idx<len(msg):
		temp = temp + msg[idx]
#		print(temp)
		if temp in dict:
			idx = idx + 1
		else:
			answer.append(dict[temp[:-1]])
			dict[temp]= cnt
			cnt = cnt + 1
			temp = msg[idx]
			idx = idx + 1
	if temp:
		answer.append(dict[temp])

#	import pprint
#	pprint.pprint(dict)
	return answer
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
