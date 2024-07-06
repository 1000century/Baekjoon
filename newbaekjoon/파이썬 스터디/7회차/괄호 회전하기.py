def check(s):
	q = []
	if s[0] not in '[({':
		return 0
	q.append(s[0])

	for i in range(1,len(s)):
		if s[i] in  '({[':
			q.append(s[i])
		else:
			if s[i] == ')' and q and q[-1] == '(':
				q.pop()
			elif s[i] == '}' and q and q[-1] == '{':
				q.pop()
			elif s[i] == ']' and q and q[-1] == '[':
				q.pop()
			else:
				return 0

	if len(q) == 0:
		return 1
	else:
		return 0

def solution(s):
	ans = 0
	for i in range(len(s)):
		ns = s[i:] + s[:i]
		ans = ans + check(ns)
	return ans

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))