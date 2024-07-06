k = int(input())
X = input().split()

def back(A,k,X,arr):
	global isitend
	if len(arr) == k+1:
		if isitend == None:
			isitend = 1
			print(*arr, sep='')
		return
	for a in range(0,k+1):
		i = A[a]
		if visited[i] == False:
			if (len(arr)==0) or ((X[len(arr)-1]=="<" and arr[-1] <A[a]) or
					 		  (X[len(arr)-1] == ">" and arr[-1] >A[a])):
				visited[i] = True
				back(A,k,X,arr+[i])
				visited[i] = False
isitend = None
maxbacktrack = [i for i in range(9,-k+8,-1)]
visited = {}
for i in maxbacktrack:
	visited[i] = 0
back(maxbacktrack,k,X,[])

isitend = None
minbacktrack = [i for i in range(0,k+1)]
visited = {}
for i in minbacktrack:
	visited[i] = 0
back(minbacktrack,k,X,[])

