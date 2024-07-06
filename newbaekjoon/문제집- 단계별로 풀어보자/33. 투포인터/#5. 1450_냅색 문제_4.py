# 시도 1) dp 2차원 리스트 시간초과
# 시도 2) dp 1차원 리스트 2개 > 시간초과
# 시도 3) meet in the middle(조합 내장함수) + 이중 포문 >> 24% 시간초과
# 시도 4) meet in the middle(조합 내장함수) + bisect 내장함수 >> 통과

from itertools import combinations
from bisect import bisect_right
N, C = map(int,input().split())
things = list(map(int,input().split()))

things.sort()

thingsA = things[:N//2]
thingsB = things[N//2:]

subA = []
for i in range(0,len(thingsA)+1):
	for li in list(combinations(thingsA,i)):
		if sum(li) <=C:
			subA.append(sum(li))
subA.sort()
subB = []
for i in range(0,len(thingsB)+1):
	for li in list(combinations(thingsB,i)):
		if sum(li) <=C:
			subB.append(sum(li))
subB.sort()

count = 0

for i in subA:
	j = bisect_right(subB,C-i)
	count = count + j
print(count)

