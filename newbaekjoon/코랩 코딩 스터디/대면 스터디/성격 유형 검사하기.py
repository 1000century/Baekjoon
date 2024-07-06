# (세현)
def solution(survey, choices):
	answer = ''
	
	# 성격 유형 점수 딕셔너리
	temper = {}
	for i in "RTCFJMAN":
		temper[i] = 0
	
	# 딕셔너리에 점수 넣기
	for i in range(len(survey)):
		if choices[i] >4:
			temper[survey[i][1]] = temper[survey[i][1]] + (choices[i]-4)
		else:
			temper[survey[i][0]] = temper[survey[i][0]] + 4-choices[i]

	# 성격유형 판단
	if temper["R"] >=temper["T"]:
		answer = answer + "R"
	else:
		answer = answer + "T"

	if temper["C"] >=temper["F"]:
		answer = answer + "C"
	else:
		answer = answer + "F"

	if temper["J"] >=temper["M"]:
		answer = answer + "J"
	else:
		answer = answer + "M"

	if temper["A"] >=temper["N"]:
		answer = answer + "A"
	else:
		answer = answer + "N"
		
	return answer