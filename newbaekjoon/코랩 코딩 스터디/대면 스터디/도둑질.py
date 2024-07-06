# (세현)
def solution(money):
	money = [0,0]+money
	coinone = [0]*(len(money))

	# 첫번째 집 털기
	coinone[2] = money[2]
	for i in range(3,len(money)-1):
		coinone[i] = max(coinone[i-2]+money[i],coinone[i-1])
	ans = max(coinone[-3],coinone[-2])

	# 첫번째 집 안털기
	cointwo = [0]*(len(money))
	for i in range(3,len(money)):
		cointwo[i] = max(cointwo[i-2]+money[i],cointwo[i-1])
	ans = max(ans,cointwo[-1],cointwo[-2])
	return ans
solution([1,2,3,1])