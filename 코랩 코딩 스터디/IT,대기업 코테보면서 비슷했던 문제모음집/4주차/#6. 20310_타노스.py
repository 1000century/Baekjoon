# (세현)

S = list(input())

one,zero = [],[]
for i in range(len(S)):
	if S[i] == "0":
		zero.append(i)
	else:
		one.append(i)

for i in range(len(one)//2):
	S[one[i]] = " "
for i in range(len(zero)//2):
	S[zero[len(zero)-1-i]] = " "

ans = ""
for i in S:
	if i != " ":
		ans = ans+i

print(ans)