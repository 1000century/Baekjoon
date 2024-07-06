"""
24.03.12
수학적으로 풀기 실패
"""
import math
N,M,B = map(int,input().split())
A= []
S = []
hap = 0
for _ in range(N):
	X = list(map(int,input().split()))
	hap = hap + sum(X)
	A.extend(X)
A.sort(reverse= True)

S.append(0)
for i in range(N-1):
	a = A[i]
	S.append(S[-1]+a)
	# 걸리는 시간 3*S[-1]-hap+(N-i-1)x
	# 필요한 블럭수 2*S[-1] -hap+N*x
	x0 = math.ceil((hap-3*S[-1])/(N-i-1)) #걸리는 시간이 0보다 크다면:
	if x0 >= 0 and 2*S[-1] -hap + N *x0 <=B:
		print(x0,3*S[-1]-hap+(N-i-1)*x0)
		





