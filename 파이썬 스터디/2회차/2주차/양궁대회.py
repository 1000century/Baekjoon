"""
양궁 대회
https://school.programmers.co.kr/learn/courses/30/lessons/92342
"""

from itertools import combinations_with_replacement

def solution(n, info):
	diff = 0
	answer = []
	cnt = 0
	for temp in combinations_with_replacement([i for i in range(11)],n):
		cnt = cnt + 1
		ryan = []
		for i in range(10,-1,-1):
			ryan.append(list(temp).count(i))
		r,a = 0,0
		for i in range(11):
			if ryan[i]==info[i]==0:
				continue
			if ryan[i]>info[i]:
				r = r+(10-i)
			else:
				a = a+(10-i)
		if r-a>diff:
			answer =ryan
			diff = r-a
	if diff == 0:
		return [-1]
	else:
		return answer

#print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]	))