# (세현)

def solution(id_list, report, k):
	answer = []
	who_blamed_me = {i:set() for i in id_list}
	mail_cnt = {i:0 for i in id_list}

	for text in report:
		a,b = text.split()
		who_blamed_me[b].add(a)

	for i in who_blamed_me:
		if len(who_blamed_me[i])>=k:
			for x in who_blamed_me[i]:
				mail_cnt[x] = mail_cnt[x]+1

	for i in id_list:
		answer.append(mail_cnt[i])
	return answer