"""
24.03.12
"""
N,M,B = map(int,input().split())
A= []
for _ in range(N):
	A.extend(list(map(int,input().split())))


for h in range(0,256):
	time = 0
	temp_block = B
	which_time = 999999999
	go = "not yet"
	for i in range(len(A)):
		a = A[i]
		if a<h: ## 놓기
			time = time + (h-a)

			temp_block = temp_block - (h-a)
			if temp_block<0 and i<len(A):
				go = "go out"
				break
				
		elif a>h: ## 뺴기
			time = time + 2*(a-h)
	if go == "go out":
		break
	else:
		if min(time,which_time) == time:
			which_time = time
			ans_time = time
			ans_height = h
print(ans_time,ans_height)
