def gcd(a,b):
	while b != 0:
		a,b = b,a%b
	return a

import math

def solution(w,h):
	w,h = max(w,h),min(w,h)
	g = gcd(w,h)

	긴,짧 = w//g, h//g # 최소단위 가로,세로 길이

	cnt= 0
	before = 0
	for 선 in range(1,짧+1):
		after = 선 * 긴 / 짧 # 이 부분...(4번,17번)
		cnt = cnt + (math.ceil(after) - before)
		before = int(after)
	return 	w*h-cnt*g

print(solution(2,3))