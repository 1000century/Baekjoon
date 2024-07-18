"""
괄호 변환
https://school.programmers.co.kr/learn/courses/30/lessons/60058
"""
def solution(p):
	answer = ''
	# 단계 1
	# 빈 문자열인 경우
	if p =='':
		return ''
	# 단계 2
	# u,v로 변환(단, u는 균형잡힌 문자열)
	u = ''
	v = p
	cnt = 0
	for idx in range(len(p)):
		i = p[idx]
		if i == "(":
			cnt = cnt + 1
		else:
			cnt = cnt - 1
		
		if cnt == 0:
			u = p[:idx+1]
			v = p[idx+1:]
			break
	
	# 단계 3,4
	# 만약 올바른 문자열이라면 for문을 끝까지 돌게 되며 다 돌았을 때의 cnt = 0
	# 만약 올바르지 않은 문자열이라면 cnt가 음수가 되는 순간 바로 break
	cnt = 0
	for i in u:
		if i == "(":
			cnt = cnt + 1
		else:
			cnt = cnt - 1
		if cnt < 0:
			break

	if cnt == 0: 	# 단계 3 u가 올바른 괄호 문자열이 아니라면
		return u + solution(v)
	else: 	# 단계 4 u가 올바른 괄호 문자열이 아니라면
		nu = ''
		for i in range(1,len(u)-1):
			if u[i] == "(":
				nu = nu + ")"
			else:
				nu = nu + "("
		u = nu
		return "("+solution(v)+")"+u

print("1-----------------------------")
print(solution("(()())()"))
print()
print("2-----------------------------")
print(solution(")("))
print()
print("3-----------------------------")
print(solution("()))((()"	), "정답","()(())()")

