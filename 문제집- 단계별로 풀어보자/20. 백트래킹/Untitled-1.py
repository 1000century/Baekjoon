def converter(num,D):
	A = ""
	while num//D != 0:
		str = "{}".format(num%D)
		A = str + A
		num = num // D
		last = num % D
		D_str = "{}".format(last)
	A = D_str + A
	return A
print(converter(31,5))