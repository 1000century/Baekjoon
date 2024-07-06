# (세현)

from bisect import bisect_left, bisect_right

N, T, P = map(int,input().split())
if N ==0:
	print(1)
	exit()
score = list(map(int,input().split()))
score.sort()
if N-bisect_left(score,T) ==P:
	print(-1)
else:
	ans = bisect_right(score,T)
	print(N-ans+1)