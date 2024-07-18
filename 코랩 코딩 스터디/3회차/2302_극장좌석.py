N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

dp = []

for i in range(1,N+1):
	if len(dp) >=2:
		if i not in vips and i-1 not in vips:
			dp.append(dp[-1]+dp[-2])
		else:
			dp.append(dp[-1])
	else:
		if len(dp) == 1:
			if 2 in vips or 1 in vips:
				dp = [1,1]
			else:
				dp = [1,2]
		elif len(dp) == 0:
			dp = [1]
if N == 1:
	print(1)
else:
	print(dp[-1])

