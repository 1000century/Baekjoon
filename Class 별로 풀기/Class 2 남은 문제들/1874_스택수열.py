"""
시작시간 : 24.03.10 22:10~22:35
7% 지나는 중
14% 지나는 중
21% 지나는 중
28% 지나는 중

근데 뭔가 딱 어떻게 푸는 거 인지는 모르겠음

"""
N = int(input())
X = []
for _ in range(N):
	X.append(int(input()))

Y = []
temp = []
ans = []
push = 1
for i in range(N):
	while push != N+2:
		if len(Y) ==0:
			Y.append(push)
			ans.append("+")
#			print("+", push, "A")
			push = push + 1

		elif X[i] == Y[-1]:
			temp.append(Y.pop(-1))
			ans.append("-")
#			print("-")
			break
		else:
			Y.append(push)
			ans.append("+")
#			print("+", push, "B")
			push = push + 1
#print(temp)
if len(temp) != N:
	print("NO")
else:
	for i in ans:
		print(i)


			


		