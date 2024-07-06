dp = [1] * 10001
for i in range(1,10001):
	d = i
	while i >0:
		d = d + i%10
		i = i//10
	if d <=10000:
		dp[d] = 0
for i in range(1,10001):
	if dp[i] == 1:
		print(i)