### 시간초과시간초과시간초과 재귀안쓰더니 안되네

N,M = map(int,input().split())

A = []
for i in range(1,N+1):
	A.append(i)
visited = [False] * (len(A) + 1)


def numbers(X,count,visited,string):
	next = str(X[0])
	string = str + next
	count = count - 1
	if count ==0:
		return string
	

numbers(A,M,"")