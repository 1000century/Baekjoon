N = int(input())
ans = 0
for _ in range(N):
	a,b,c = map(int,input().split())
	if a == b == c:
		ans = max(ans,10000+a*1000)
	elif a != b and b != c and c!=a:
		ans = max(ans,max(a,b,c)*100)
	else:
		if a == b:
			k = a
		elif b == c:
			k = b
		else:
			k = c
		ans = max(ans,1000+k*100)
print(ans)
