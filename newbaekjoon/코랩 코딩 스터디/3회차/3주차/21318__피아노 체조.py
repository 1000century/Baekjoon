# (세현)
import sys
input = sys.stdin.readline

N = int(input())
ezpz = list(map(int,input().split()))+[int(1e9)]

ans = [0]*(N+1)
for i in range(N):
	ans[i+1] = ans[i]+(ezpz[i]>ezpz[i+1])

for _ in range(int(input())):
	x,y = map(int,input().split())
	print(ans[y-1]-ans[x-1])