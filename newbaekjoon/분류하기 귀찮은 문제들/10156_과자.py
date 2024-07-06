"""
과자
https://www.acmicpc.net/problem/10156
"""

k,n,m = map(int,input().split())

ans = m-n*k

if ans >0:
	print(0)
else:
	print(-ans)