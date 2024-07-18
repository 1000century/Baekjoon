# (세현)
"""
24.03.11
35%에서 틀림 25%에서 틀림 47%에서 틀림 75프로에서 틀림

나타날 수 있는 오류들
1. 나누는 수가 0이 되는 오류
2. 가장 큰점(maxi)을 건너뛰게 되는 오류
"""

import sys
K,N = map(int,sys.stdin.readline().split())
X = []
for _ in range(K):
	X.append(int(sys.stdin.readline()))

start = 1
end = sum(X) // K
ans = 0

while start<=end:
	middle = (start + end) // 2
	count = sum([x//middle for x in X])
 
	if count >= N:
		start = middle + 1
		ans = middle

	else:
		end = middle - 1
    
print(ans)