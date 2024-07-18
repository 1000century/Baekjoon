from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))

A.sort()
cnt = 0
for target in range(N):
	isit = 0
	for num_1 in range(N):
		if num_1 ==target:
			continue
		num_2 = bisect_left(A,A[target]-A[num_1])
		while num_2<N:
			if num_2 ==target or num_2 ==num_1:
				num_2 = num_2 + 1
				continue
			if A[target] < A[num_1] + A[num_2]:
				break
			elif A[target] == A[num_1] + A[num_2]:
				isit = 1
				break
			num_2 = num_2 + 1
		if isit == 1:
			cnt = cnt + 1
			break
print(cnt)