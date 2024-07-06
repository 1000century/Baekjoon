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
for i in range(2500):
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
diameter = (r_squ**0.5)*2
import math
def solution(value):    # 입력값을 100배 증가
    scaled_value = value * 100
    
    # 반올림
    if scaled_value - math.floor(scaled_value) < 0.5:
        result = math.floor(scaled_value)
    else:
        result = math.ceil(scaled_value)
    
    # 원래 스케일로 돌아가기 위해 100으로 나눔
    return result / 100
ans = solution(diameter)
		
		
print(f'{ans:.2f}')
