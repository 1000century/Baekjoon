N = int(input())
x = 1
t = 10
div = 1
while N!= 0:
	x = x*(t)
	t = t + 1
	div = div*N
	N = N -1
print((x//div)%10007)