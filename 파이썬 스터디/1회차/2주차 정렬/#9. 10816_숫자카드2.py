"""
이분탐색보다는 dictionary로 푸는 게 좋은듯

이 문제는 왜 분류가 "정렬"이지?
>>> 그나마 계수정렬??/
"""

N = int(input())
X  = list(map(int,input().split()))

i_have = {}
for x in X:
	if i_have.get(x) ==None:
		i_have[x] = 1
	else:
		i_have[x] = i_have[x] + 1

M = int(input())
Y = list(map(int,input().split()))
for y in Y:
	if i_have.get(y) ==None:
		print(0,end = " ")
	else:
		print(i_have[y],end= " ")