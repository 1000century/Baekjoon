def convert(num, base):
	temp = "0123456789ABCDEF"
	q= num//base
	r = num% base
	if q == 0:
		return temp[r]
	else:
		# q를 base로 변환
		# 즉, n진수의 다음 자리를 구함
		return convert(q, base) + temp[r]
	
def solution(n, T, M, p):
	answer = ''
	test = ''
	
	for i in range(M*T):
		test = test + str(convert(i, n))
		
	while len(answer) < T:
		answer = answer + test[p-1]
		p = p + M
		
	return answer