# (세현)

def blog():
	N, X = map(int,input().split())
	visitor = list(map(int,input().split()))

	sumvisitor = [visitor[0]] # 부분합 할 때 첫항 따로 빼두기
	for i in range(1,len(visitor)):
		sumvisitor.append(visitor[i]+sumvisitor[-1])
	
	# 조회수 0명인 경우
	if sumvisitor[-1] == 0:
		print("SAD")
		return
	
	# 조회수 0명이 아닌 경우
	ans = sum(visitor[:X])  # 부분합 할 때 첫항 따로 빼두기
	count = 1
	for i in range(X,len(sumvisitor)):
		if ans<sumvisitor[i]-sumvisitor[i-X]:
			ans = sumvisitor[i]-sumvisitor[i-X]
			count = 1
		elif ans==sumvisitor[i]-sumvisitor[i-X]:
			count = count + 1

	print(ans)
	print(count)
	return

blog()