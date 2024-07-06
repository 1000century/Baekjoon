"""
key값을 넣을 때랑 없을 때랑 sort()의 차이가 있다.
"""

N = int(input())
array = []
for _ in range(N):
	array.append(list(map(int,input().split())))
array.sort()

for i in array:
	print(i[0],i[1])