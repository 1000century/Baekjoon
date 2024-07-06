"""
stdin을 쓰면 오히려 시간이 오래 걸리는...?
"""

import sys
tests = []
while True:
	a = input()
	if a == "-1 -1 -1":
		break
	else:
		tests.append(list(map(int,a.split())))

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
	if a<=0 or b <=0 or c <=0:
		return 1
	if a >20 or b > 20 or c > 20:
		return w(20,20,20)
	
	if dp[a][b][c]:
		return dp[a][b][c]
	
	if a <b and b<c:
		dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
		return dp[a][b][c]

	dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
	return dp[a][b][c]

for test in tests:
	a,b,c = test[0], test[1], test[2]
	x = w(a,b,c)
	print(f"w({a}, {b}, {c}) = {x}")