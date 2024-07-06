B,A = map(int,input().split())


B = B - 1
a = A + 1
b = B + 1

sum_a = 0
count_a = 0

while True:
	a_2 = a // (2**(count_a+1))
	a_3 = a % (2**(count_a+1))
	a_4 = a_3 - (2**count_a)
	if a_4 > 0:
		sum_a = sum_a + a_4
		

	
	sum_a = sum_a + a_2 * (2**count_a)
	
	if a_2 <= 1:
		sum_a = sum_a + a_3
		break
	else:
		count_a = count_a + 1


sum_b = 0
count_b = 0

while True:
	b_2 = b // (2**(count_b+1))
	b_3 = b % (2**(count_b+1))
	b_4 = b_3 - (2**count_b)
	if b_4 > 0:
		sum_b = sum_b + b_4
		

	
	sum_b = sum_b + b_2 * (2**count_b)
	
	if b_2 <= 1:
		sum_b = sum_b + b_3
		break
	else:
		count_b = count_b + 1
	
if A == 1:
	sum_a = 1
if B == 0:
	sum_b = 0

print(sum_a-sum_b)


