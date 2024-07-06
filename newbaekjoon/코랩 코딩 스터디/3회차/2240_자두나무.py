T,W = map(int,input().split())


tree = []
now = 1
cnt = 0
ans = [[[0,0]]*W for _ in range(T+1)]
print(ans)
for i in range(1,T+1):
	x = int(input())
	for w in range(W):
		if x == 0 and now == 0:
			ans[i][w][0] = ans[i-1][w][0]+1
			ans[i][w][1] = ans[i-1][w][1]

		elif x == 0 and now == 1:
		
		elif x == 1 and now == 0:
		
		elif x == 1 and now == 1:
			


