"""
순서가 상관있기 때문에 배낭문제 풀듯이 풀면 안됨.
(실패)
"""

H,y = map(int,input().split())

Y = [0]*(y+1)
Y[0] = H

products = [(1,1.05),(3,1.2),(5,1.35)]
for (yr,rate) in products:
	for i in range(yr,y+1):
		Y[i] = max(Y[i], int(rate*Y[i-yr]))
		print(Y)
print(Y[-1])