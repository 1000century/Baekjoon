### 시간초과시간초과시간초과 재귀안쓰더니 안되네

N,M = map(int,input().split())


B = N + 1 # B진법(1,2,3,...N=B-1까지)

end_num = 0
i = 1
while i != M+1:
	end_num += N * (N+1)**(M-i)
	i = i + 1

def converter(num,D):
	A = ""
	D_str = "{}".format(num)
	while num//D != 0:
		str = "{}".format(num%D)
		A = str + A
		num = num // D
		last = num % D
		D_str = "{}".format(last)
	A = D_str + A
	return A

J = 1
while J != end_num+1:
	result = ""
	total = converter(J,B)
	total_list = list(total)
	if len(total_list) == len(list(set(total_list))) and len(total_list) == M and "0" not in total_list:
		result = " ".join(total)
		print(result)
		J = J + 1
	else:
		J = J + 1

	