"""
메뉴리뉴얼
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""
from itertools import combinations
def solution(orders, course):
	answer = []
	food = {}
	for c in course:
		count = 2
		ans = set()
		for i in orders:
			for a in combinations(sorted(i),c):
				
				# 딕셔너리에 문자열 넣기
				if a not in food:
					food[a] = 0
				food[a] = food[a] + 1

				# 코스에 추가할 수 있다면 추가하기
				if food[a] > count:
					count = food[a]
					ans = set(''.join(a))
				if food[a] == count:
					ans.add(''.join(a))
		for t in ans:
			answer.append(t)
			
	answer.sort()			

	return answer

#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))