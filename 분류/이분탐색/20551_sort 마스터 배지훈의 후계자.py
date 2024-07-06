"""
24.03.17 02:39~02:51
python3 stdin 안쓰면 시간초과
"""
import sys
N,M = map(int,sys.stdin.readline().split())
A=[]
for _ in range(N):
	A.append(int(sys.stdin.readline().rstrip()))
B = sorted(A)
# print(B)

def isit(B,D):
	low = 0
	high = len(B)-1 # 닫힌구간
	while low <=high:
		mid = (low+high)//2
		if D<=B[mid]:
			high = mid -1
		else:
			low = mid + 1
	if low!= N and B[low] == D:
		return low
	else:
		return -1
for _ in range(M):
	D = int(sys.stdin.readline().rstrip())
	print(isit(B,D))
