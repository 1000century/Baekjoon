N = int(input())
P = list(map(int,input().split()))
M = int(input())

a = P.index(min(P))

if a != 0:
	최대자릿수 = M//P[a]
elif len(P) != 1:
	b = P.index(min(P[1:]))
	x = M-P[b]
	if x<0:
		최대자릿수 = 0
	else:
		최대자릿수 = 1 + x//P[a]
else: # 끝에서 런타임에러
	최대자릿수 = 0
#print(최대자릿수)

if 최대자릿수 == 0:
	print(0)
	exit()

x = ''

for i in range(최대자릿수-1,-1,-1):
	for n in range(N,0,-1):
		if M >=P[n-1] + P[a]*i:
			x = x+str(n-1)
			M = M-P[n-1]
			break
print(x)