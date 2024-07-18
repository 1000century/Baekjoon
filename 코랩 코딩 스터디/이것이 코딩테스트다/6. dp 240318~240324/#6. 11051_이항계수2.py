# (세현)
# 직접적인 나눗셈 대신 곱셈의 역원을 사용하는 방법(?)

N,K = map(int,input().split())
p = min(K,N-K) # nCp

A = [1] * (p+1)

for i in range(1,p+1):
	A[i] = A[i-1]*(N+1-i)//i

print(A[p]%10007)