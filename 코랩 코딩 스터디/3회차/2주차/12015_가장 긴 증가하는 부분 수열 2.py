# https://maramarathon.tistory.com/57
"""
DP로 LIS의 길이를 구하는 경우, 시간 복잡도는 O(N^2)이 된다.
이분탐색으로 LIS의 길이를 구하는 경우, 시간 복잡도는 O(NlogN)이 된다.

>> LIS 길이 뿐 아니라 자체를 구할 수도 있어야함
"""
from bisect import bisect_right,bisect_left
N = int(input())
A = list(map(int,input().split()))
dp = [A[0]]
ans = 1
for i in range(1,N):
	if A[i]>dp[-1]:
		dp.append(A[i])
		ans = ans + 1
		continue
	idx = bisect_left(dp,A[i])
	dp[idx] = A[i]
#print(A)
print(ans)
#print(len(A))

