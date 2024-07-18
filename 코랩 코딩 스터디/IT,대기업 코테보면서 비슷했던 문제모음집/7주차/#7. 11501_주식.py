# (세현)

# 시도 1) bfs
# 시도 2) 그리디
import sys
input = sys.stdin.readline
def solution2(N,cir):
	best = cir[-1]
	ans = 0
	for i in reversed(cir):
		ans = ans + max(0,best-i)
		best = max(best,i)
	print(ans)

T = int(input())
for _ in range(T):
	N = int(input().strip())
	cir = list(map(int,input().strip().split()))
	solution2(N,cir)