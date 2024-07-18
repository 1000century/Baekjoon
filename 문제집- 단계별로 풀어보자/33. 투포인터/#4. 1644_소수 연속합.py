from collections import deque
N = int(input())

# N = 1일 때 처리 안해두면 98%즈음에서 indexerror
if N ==1:
	print(0)
	exit()


# 첫 소수 2를 넣고 시작
li = [2] # 이후에도 사용되는 소수 리스트
q = deque([2]) # 소수 찾는 데에만 쓰이는 deque
dp = [1]*(N+1) # 소수 찾는 데에만 사용 됨
dp[2] = 0

while q:
	x = q.popleft()
	for i in range(1,N//x+1):
		if i == 1:
			continue
		dp[x*i] = 0
	for j in range(x+1,N+1): # x 다음 소수 찾기
		if dp[j] == 1:
			q.append(j)
			li.append(j) 
			break

#print(li)


lt, rt  = 0,0
numsum = 0
count = 0
while True:
	if numsum == N:
		count = count + 1
	if numsum >=N:
		numsum = numsum -li[lt]
		lt = lt + 1
	elif rt == len(li): # 이 부분이 조금 불편
		break
	else:
		numsum = numsum +li[rt]
		rt = rt + 1
print(count)
