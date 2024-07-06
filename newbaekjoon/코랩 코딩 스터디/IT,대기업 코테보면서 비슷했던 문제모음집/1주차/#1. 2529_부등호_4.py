k = int(input())
X = input().split()

def back(k,X,arr,visited=[0]*(10)):
	if len(arr) == k+1:
		string = ''.join(str(i) for i in arr)
		result.append(string)
		return

	for i in range(0,10):
		if visited[i] == False:
			if (len(arr)==0) or ((X[len(arr)-1]=="<" and arr[-1] <i) or
					 		  (X[len(arr)-1] == ">" and arr[-1] >i)):
				visited[i] = True
				back(k,X,arr+[i],visited)
				visited[i] = False

result = []
back(k,X,[])
result.sort()

print(result[-1],result[0],sep='\n')
