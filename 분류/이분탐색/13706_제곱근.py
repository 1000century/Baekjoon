"""
24.03.17 02:51

isqrt 쓰라고 하네
"""

N = int(input())

start = 1
end = N
while start<=end:
	mid = (start+end)//2
	if mid * mid == N:
		print(int(mid))
		break
	elif mid * mid >N:
		end = mid -1
	else:
		start = mid + 1
