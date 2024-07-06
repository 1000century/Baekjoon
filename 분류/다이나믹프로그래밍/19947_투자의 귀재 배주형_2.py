"""
순서가 상관있기 때문에 배낭문제 풀듯이 풀면 안됨.

1111 * 1.2 = 1333.2
1333.2 * 1.05 = 1399.86

"""

H,y = map(int,input().split())

account = [H]*(y+1)

products = [(1,1.05),(3,1.2),(5,1.35)]
for i in range(1,y+1):
	temp = [account[i-1]]
	if i >=1:
		temp.append(int(account[i-1]*1.05))
	if i>=3:
		temp.append(int(account[i-3]*1.2))
	if i>=5:
		temp.append(int(account[i-5]*1.35))
		
	account[i] = max(temp)
print(account[-1])