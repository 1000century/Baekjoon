# (세현)
# 주식(11501)과 같은 문제 - 그리디

import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
price= list(map(int,input().split()))

lowest = price[0]
ans = 0
for i in range(len(road)):
	ans = ans + road[i]*lowest
	lowest = min(lowest,price[i+1])
print(ans)