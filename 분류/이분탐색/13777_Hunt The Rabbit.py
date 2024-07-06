"""
24.03.17 19:40~19:56
솔직히 범위설정하는 거 꽤 헷갈렸음
"""
while True:
	N = int(input())
	if N == 0:
		break

	st = 1
	en = 50
	while st<=en:
		mid = (st + en) // 2
		print(mid,end = " ")
		if mid ==N:
			print()
			break
		else:
			if mid < N:
				st = mid + 1
			else:
				en = mid - 1

