
"""
09:49~10:01 시간초과
10:01~1003 9960ms
stdout으로 바꾸니까 >> 7896ms

import copy
<복사하는 법>
``copy.deepcopy
X = nums[:]
swap 함수 (x,y) > (y,x)
"""
import sys
N, M, q = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
	arr.append(list(map(int,sys.stdin.readline().split())))


for _ in range(q):
	quary = list(map(int,sys.stdin.readline().split()))
	if quary[0] == 0: #첫번째 쿼리
		a = quary[1]
		b = quary[2]
		k = quary[3]
		arr[a][b] = k
	else: # 두 번째 쿼리
		a = quary[1]
		b = quary[2]
		if a > b:
			arr.insert(b,arr[a])
			arr.insert(a+1,arr[b+1])
			del arr[b+1]
			del arr[a+1]

		elif a < b:
			arr.insert(a,arr[b])
			arr.insert(b+1,arr[a+1])
			del arr[a+1]
			del arr[b+1]

for x in arr:
    for y in x:
        sys.stdout.write(str(y) + " ")
    sys.stdout.write("\n")



