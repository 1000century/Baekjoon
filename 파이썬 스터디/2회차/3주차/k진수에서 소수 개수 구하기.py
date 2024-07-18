"""
k진수에서 소수 개수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""

def sosu(a):
	if a == 1: return 0
	for i in range(2,int(a**0.5)+1):
		if a % i ==0: return 0
	return 1
		
def solution(n, k):
	# 1. 진법 변환
	s = ''
	while n != 0:
		s = str(n%k)+s
		n = n//k

	# 2. 소수 후보가 될 수 있는 것들 찾기!
	cand = list(s.split('0'))
	
	# 3. 후보들 중에 소수 찾기
	answer = 0
	for i in cand:
		if i !='':
			answer = answer + (sosu(int(i)) == 1)

	return answer

print(solution(437654,3))
print(solution(110011,10))