n,b = map(int,input().split())
dots = []
for _ in range(n):
	x,y = map(int,input().split())

sx = sum(x[0] for x in dots)
sy = sum(x[1] for x in dots)

up = sy-n*b
down = sx

if 