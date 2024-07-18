N = int(input())
count = -1

X = list(list(map(int,input().replace(""," ").split())) for _ in range(N))
print(X)


def quad(h, x, n):
	if n == 1:
		return X[h][x]
	else:
		LU = quad(h, x, n//2)
		LD = quad(h+n//2, x, n//2)
		RU = quad(h, x+n//2, n//2)
		RD = quad(h+n//2, x+n//2, n//2)
		if str(LU)[0] != "(" and str(RU)[0] != "(" and str(LD)[0] != "(" and str(RD)[0] != "("and LU ==LD == RU == RD:
			return LU
		else:
			return "(" +str(LU)  + str(RU) + str(LD) + str(RD)+")"

print(quad(0,0,N))

