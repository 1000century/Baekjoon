T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

SA,SB = [0],[0]
FA,FB = [],[]
for i in A:
	SA.append(SA[-1]+i)
for i in range(n+1):
	for j in range(i+1,n+1):
		FA.append(SA[j]-SA[i])
for i in B:
	SB.append(SB[-1]+i)
for i in range(m+1):
	for j in range(i+1,m+1):
		FB.append(SB[j]-SB[i])

FA.sort()
FB.sort()
ans = 0
from bisect import bisect_left,bisect_right
for i in FA:
	rt,lt = bisect_right(FB,T-i),bisect_left(FB,T-i)
	if lt<len(FB) and T-i == FB[lt]:
		ans = ans + rt-lt

print(ans)