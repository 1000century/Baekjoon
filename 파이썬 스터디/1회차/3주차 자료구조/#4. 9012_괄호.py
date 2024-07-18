import sys
N = int(sys.stdin.readline().rstrip())

answers = []

for _ in range(N):
	case = list(sys.stdin.readline().rstrip())
	count = 0
	ans = "YES"
	for i in case:
		if i == "(":
			count = count + 1
		else:
			if count != 0:
				count = count - 1
			else:
				ans = "NO"
				break
	if count != 0:
		ans = "NO"
	answers.append(ans)

# gpt한테 물어보니까 이거 자체가 표준 printout이라고 함...
print(*answers, sep='\n') 