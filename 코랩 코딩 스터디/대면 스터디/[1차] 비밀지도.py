def solution(n, arr1, arr2):
	answer = []
	for i in range(n):
		row = ""
		for j in range(n-1,-1,-1):
			if arr1[i]% 2 == 1 or arr2[i]%2 == 1:
				row = "#"+row
			else:
				row = " "+row
			
			arr1[i], arr2[i] = arr1[i] //2, arr2[i] //2

		answer.append(row)
			
	return answer

print("----------------test 1")
n = 5
arr1 =	[9, 20, 28, 18, 11]
arr2 =	[30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))

print("------------------test2")
n	=6
arr1=	[46, 33, 33 ,22, 31, 50]
arr2=	[27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))
