def rotate(arrs,x1,x2,y1,y2):
	A  =[]
	A.extend([[x1,y] for y in range(y1,y2)])
	A.extend(list([x,y2] for x in range(x1,x2)))
	A.extend(list([x2,y] for y in range(y2,y1,-1)))
	A.extend(list([x,y1] for x in range(x2,x1, -1)))
	이전값 = arrs[A[0][0]][A[0][1]]
	x = 이전값
	for i in range(1,len(A)):
		다음값 = arrs[A[i][0]][A[i][1]]
		arrs[A[i][0]][A[i][1]]=이전값
		이전값 = 다음값
		x = min(x,이전값)

	arrs[A[0][0]][A[0][1]] = 이전값
	return arrs,x

def solution(rows, columns, queries):
	ans = []
	arr = [[0]*columns for _ in range(rows)]
	for i in range(rows):
		for j in range(columns):
			arr[i][j] = (i)*columns+j+1
	for x1,y1,x2,y2 in queries:
		arr,p = rotate(arr,x1-1,x2-1,y1-1,y2-1)
		ans.append(p)
		
	return ans



print()
print('33333333333333333333333333333')
rows,columns = 6,6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	
print(solution(rows,columns,queries))

print()
print('33333333333333333333333333333')
rows,columns = 3,3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows,columns,queries))

print()
print('33333333333333333333333333333')
rows, columns = 100,97
queries = [[1,1,100,97]]	
print(solution(rows,columns,queries))