# (세현)
# Counter 도입하니까 바로 풀림

from collections import Counter
def solution(a,b):
	A = Counter([i for i in a])
	B = Counter([i for i in b])

	diff = sum(A.values())+sum(B.values())
	for i in A:
		if i in B:
			diff = diff - 2*min(A[i],B[i])

	# diff == 0 >> 같은 구성인 경우
	# diff == 1 >> 비슷한 구성(문자 한 개를 더하거나 빼기)
	# diff == 2 & len(a)==len(b) >> 비슷한 구성(문자 한 개를 바꾸기)
	if diff <=1 or (diff == 2 and len(a)==len(b)):
		return 1
	return 0

n = int(input())
a = input()

ans = 0
for _ in range(n-1):
	b = input()
	ans = ans + solution(a,b)

print(ans)