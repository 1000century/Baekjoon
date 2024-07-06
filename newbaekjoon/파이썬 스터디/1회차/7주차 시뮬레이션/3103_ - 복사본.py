import sys
sys.setrecursionlimit(100000)
K, N = map(int,input().split())
selected = list(map(int,input().split()))

factorial = [1]*K
for i in range(2,K+1):
	factorial[-i] = (factorial[-i+1]*i)%1000000007

for i in range(N):
	a,b = map(int,input().split())
	changed = selected[:]
	changed[a-1], changed[b-1] = selected[b-1], selected[a-1]
	testcase = ''
	count = 0
	visited = [0]*(K+1)
	for i in range(len(changed)-1):
		num = changed[i]
		visited[num] = 1
		tempcount= 0
		for j in range(1,num):
			if visited[j] == 1:
				tempcount = tempcount + 1

		count = count + (num-1-tempcount)*(factorial[i+1])
	for j in range(1,changed[-1]):
		if visited[j] == 0:
			count = (count + 1)%1000000007
	count = (count + 1)%1000000007
	print(count)
