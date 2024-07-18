"""
시작시간 : 24.03.10 21:13~ 22:10

이거 처음에 생각을 잘못한게 sort해서 앞뒤로 한명씩만 비교했는데
그게 아니라 순위는 나보다 큰 사람의 숫자를 세야함...
"""
N = int(input())
X = []
abcd = [0] * N
for _ in range(N):
	A = list(map(int,input().split()))
	A.append(_)
	X.append(A)

for person in X:
	count = 1
	for i in range(N):
		if X[i][1] > person[1] and X[i][0] > person[0]:
			count = count + 1
	print(count, end = " ")
		
