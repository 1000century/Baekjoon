def solution(record):
	temp = []
	chat = {}
	for sent in record:
		i = list(sent.split())
		if i[0] == "Enter":
			chat[i[1]] = i[2]
			temp.append((i[1],0))
		elif i[0] == "Change":
			chat[i[1]] = i[2]
		else:
			temp.append((i[1],1))

	ans = []
	for i in range(len(temp)):
		if temp[i][1] == 0:
			ans.append(f"{chat[temp[i][0]]}님이 들어왔습니다.")
		else:
			ans.append(f"{chat[temp[i][0]]}님이 나갔습니다.")

	return ans
