M,N = map(int,input().split())
temp = [False,False] + [True]*(N-1)

for i in range(2,N+1):
	if temp[i]:
		for j in range(i*2,N+1,i):
			temp[j] = False
for i in range(M,N+1):
	if temp[i]:
		print(i)

"""
이거 뭔가 M~N 사이에서 M이 만약에 N과 엄청 가까이 있는 수라면 리스트를 낭비하는 거 아닌가?
"""