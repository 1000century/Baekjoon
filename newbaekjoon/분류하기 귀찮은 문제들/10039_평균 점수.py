ans = 0
for _ in range(5):
	x = float(input())
	if x <40:
		x = 40
	ans = ans + x/5

print(int(ans))