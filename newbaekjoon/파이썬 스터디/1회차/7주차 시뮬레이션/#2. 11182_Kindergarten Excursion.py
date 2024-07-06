children = input()
A,B,C = 0,0,0
ans = 0
cnt = 0
for i in children:
	if i =="0":
		A = A+1
		ans = ans + B + C
	elif i == "1":
		B = B+1
	else:
		C = C+1
		ans = ans - B
		cnt = cnt + 1
print(ans + cnt*B)
