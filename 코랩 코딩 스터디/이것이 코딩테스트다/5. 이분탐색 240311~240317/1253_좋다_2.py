# (세현)
"""
24.03.15 16:41~
이분탐색 안된다.

딕셔너리 + set 이용해서 풀기
67프로에서 오류

메모리초과
"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))
collect.sort()

count = 0

dict = {}
if N ==1 or N ==2:
	print(0)
	exit()
for n in range(0,N):
	for j in range(0,n):
		if n !=j:
			sums = collect[n]+collect[j]
			if sums not in dict:
				dict[sums] = set()
			dict[sums].add((n,j))



for a in range(0,N):
	target = collect[a]
	if target in dict:
		temp = dict[target]
		for x,y in temp:
			if x != a and y!=b:
				count = count + 1
				break
print(count)



