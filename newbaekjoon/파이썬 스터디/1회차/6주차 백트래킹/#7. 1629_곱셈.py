a,b,c = map(int,input().split())
a = a%c
ans = 1
dp = []
for i in range(b):
	ans = (ans * a)%c
	if ans in dp:
		break
	else:
		dp.append(ans)
rotate = len(dp)
rest = b%rotate
print(dp[rest])