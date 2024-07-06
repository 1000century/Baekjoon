## serenie3824

N = int(input())
numlist = [i for i in range(1,N+1)]

fact = [1]*(N)
for i in range(1,N):
	fact[-i-1] = fact[-i]*i

testcase = list(map(int,input().split()))

if testcase[0] == 1: 	# 문제 1 시작
	testnum = testcase[1] - 1 # 숫자카운트가 0부터가 아니라 1부터 세기 때문
	for idx in range(N):
		a = (testnum//fact[idx])
		testnum = testnum%fact[idx]
		print(numlist[a],end=" ")
		del numlist[a]


else:	# 문제 2 시작 
	testlist = testcase[1:]
	count = 1 # 숫자카운트가 0부터가 아니라 1부터 세기 때문
	for i in range(len(testlist)):
		idx = numlist.index(testlist[i])
		count = count +(idx)*fact[i]
		del numlist[idx]
	print(count)
		