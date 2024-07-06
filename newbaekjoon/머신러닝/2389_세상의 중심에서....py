import sys
input = sys.stdin.readline
N = int(input().strip())

circle =[]
for _ in range(N):
	x,y = map(float,input().strip().split())
	circle.append((x,y))

a,b = sum(x[0] for x in circle), sum(x[1] for x in circle)

r_squ=0
for x,y in circle:
	r_squ = max(r_squ,(a-x)**2+(b-y)**2)

w = 0.1
for i in range(800):
	mr_squ = 0
	mx,my = 0,0
	for x,y in circle:
		dist = ((a-x)**2+(b-y)**2)
		if mr_squ <= dist:
			mr_squ = dist
			mx,my = x,y
	r_squ = mr_squ
	a,b = a+(mx-a)*w, b+(my-b)*w
	w *= 0.994
print(a, b, r_squ**0.5)