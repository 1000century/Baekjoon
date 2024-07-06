X = int(input())
ans = 0
for i in range(7):
#	print(bin(X),bin(1<<i))
	if X & (1<<i):
		ans = ans + 1
print(ans)
