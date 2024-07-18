n = int(input())
if n>0:
	dp = [0,1]
	while n != 1:
		dp.append((dp[-1]+dp[-2])%1000000000)
		dp = dp[1:]
		n = n-1
	
	if dp[-1]>0:
		print(1)
		print(dp[-1]%1000000000)
	elif dp[-1] == 0:
		print(0)
		print(0)
	else:
		print(-1)
		print((-dp[-1])%1000000000)
elif n<0:
	dp = [0,1]
	while n != -1:
		x = (dp[-2]-dp[-1])
		if x > 0:
			x = x%1000000000
		elif x <0:
			x = (-x)%1000000000
			x = -x
		dp.append(x)
		dp = dp[1:]
		n = n + 1
	if dp[-1]>0:
		print(1)
		print(dp[-1]%1000000000)
	elif dp[-1] == 0:
		print(0)
		print(0)
	else:
		print(-1)
		print((-dp[-1])%1000000000)

else:
	print(0)
	print(0)