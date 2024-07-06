# (세현)
"""
 파이썬의 collections.Counter 클래스는 집합 연산도 지원하는데,
 이를 이용해 두 카운터 사이의 교집합과 합집합을 구할 수 있습니다.
"""
from collections import Counter
def solution(str1, str2):
	str1= str(str1).lower()
	str2= str(str2).lower()
	subA,subB=[],[]

	for i in range(len(str1)-1):
		temp = str1[i:i+2]
		if temp.isalpha():
			subA.append(temp)

	for i in range(len(str2)-1):
		temp = str2[i:i+2]
		if temp.isalpha():
			subB.append(temp)

	A,B = Counter(subA),Counter(subB)

	inter,union = A&B, A|B
	sum_inter, sum_union = sum(inter.values()),sum(union.values())

	if sum_union == 0:
		return 65536
	else:
		return int(65536*(sum_inter/sum_union))


print("testcase")
print(solution("FRANCE","french"))
print(solution("aa1+aa2","AAAA12"))
print(solution("handshake","shake hands"))
print(solution("E=M*C^2","e=m*c^2"))