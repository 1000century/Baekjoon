def solution(s):
	ans = []
	for i in range(1,1+len(s)):
		length = ""
		cnt = 1
		temp = ''
		for j in range(len(s)//i+1):
			if len(s) /i == 0:
				continue
			if str(s[i*j+0:i*(j+1)]) == str(temp):
				cnt = cnt + 1
			else:
				if cnt >1:
					length = length + str(cnt)
				
				length = length + s[i*j+0:i*(j+1)]
				temp = s[i*j+0:i*(j+1)]
				cnt = 1
		if cnt > 1:
			length = length + str(cnt)
		ans.append((len(length),i))
	ans.sort(key = lambda x:x[0],reverse = False)
			
	return ans[0][0]
S = [
"aabbaccc",
"ababcdcdababcdcd",
"abcabcdede"	,
"abcabcabcabcdededededede"	,
"xababcdcdababcdcd"	,]
for s in S:
	print(solution(s))