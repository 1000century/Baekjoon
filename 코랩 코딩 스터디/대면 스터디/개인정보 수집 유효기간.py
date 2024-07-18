def transform(date):
	yr = int(date[0:4])
	mon = int(date[5:7])
	day = int(date[8:])

	return yr*12*28+mon*28+day

def solution(today, terms, privacies):
	today_num = transform(today)
	terms_dic = {}
	for x in terms:
		a,b = x.split()
		terms_dic[a] = int(b)
	answer = []
		
	for k in range(len(privacies)):
		i = privacies[k]
		now_date, alphabet = i.split()
		start_num = transform(now_date)
		if today_num - start_num < terms_dic[alphabet]*28:
			continue
		answer.append(k+1)

		
	
	
	
	return answer
today = "2022.05.19"
terms =	["A 6", "B 12", "C 3"]
privacies =["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms,privacies))

today = "2020.01.01"
terms =["Z 3", "D 5"]
privacies =	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms,privacies))