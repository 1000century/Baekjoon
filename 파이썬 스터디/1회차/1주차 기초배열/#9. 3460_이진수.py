T = int(input())

for _ in range(T):
	n = int(input())
	count = 0
	while True:
		if n%2 ==1:
			print(count, end = " ")
		n = n//2
		count = count + 1
		if n == 0:
			break
	print()

# bin(N) 8진수 10진수 등등 바꿀 수 있음