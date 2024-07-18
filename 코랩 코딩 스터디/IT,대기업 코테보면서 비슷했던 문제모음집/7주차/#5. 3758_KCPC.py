# (세현)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	n,k,t,m = map(int,input().split())

	score = {i:{j:0 for j in range(1,k+1)} for i in range(1,n+1)}
	count = {i:0 for i in range(1,n+1)}
	submit = {i:0 for i in range(1,n+1)}
	
	for a in range(1,m+1):
		i,j,s = map(int,input().split())
		score[i][j] = max(score[i][j],s)
		count[i] = count[i] + 1
		submit[i] = a
	
	ranking = []
	for i in range(1,n+1):
		ranking.append([sum(score[i].values()),count[i],submit[i],i])
	ranking.sort(key = lambda x:(-x[0],x[1],x[2]))

	for i in range(n):
		if ranking[i][3] == t:
			print(i+1)