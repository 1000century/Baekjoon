"""
def linear_regression(points):
    N = len(points)
    sum_x = sum(p[0] for p in points)
    sum_y = sum(p[1] for p in points)
    sum_xy = sum(p[0]*p[1] for p in points)
    sum_x2 = sum(p[0]**2 for p in points)
    
    # 기울기 a 계산
    a = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    
    # 절편 b 계산
    b = (sum_y - a * sum_x) / N
    
    return a, b
"""

import sys
input = sys.stdin.readline
N = int(input().strip())

dots =[]
for _ in range(N):
	x,y = map(int,input().strip().split())
	dots.append((x,y))
mx = sum(x[0] for x in dots)
my = sum(y[1] for y in dots)
mxy = sum(x[0]*x[1] for x in dots)
mxx = sum(x[0]*x[0] for x in dots)

a = (N*mxy-mx*my) / (N*mxx-mx*mx)
b= (my-a*mx)/N
print(f'{a:.3f}')
print(f'{b:.3f}')