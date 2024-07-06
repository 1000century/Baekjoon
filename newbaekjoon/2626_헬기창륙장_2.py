import math

def format_float(val):
	formatted = f"{val:.3f}"
	if formatted == "-0.0000":
		return "0.0000"
	return formatted
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def main():
	N = int(input())
	fan = []
	for _ in range(N):
		a, b = map(int, input().split())
		fan.append(Point(a, b))
	
	w = 0.1 # 각 단계에서 가장 먼점으로 10%씩 이동
	center = Point(0, 0)
	
	# 모든 점의 평균을 구하는 것. 여기서부터 학습 시작함.
	for i in fan:
		center.x += i.x / N
		center.y += i.y / N
	
	# Iteratively adjust center towards the furthest point ＞＞ ｗ를 학습함
	mxdist, radius = 0, 0
	for _ in range(100000):
		mxdist = 0 # 반복할 때마다 중심점과 주어진 점 집합 중 가장 먼 점 사이의 거리제곱
		mxPoint = None
		for i in fan:
			dist = (center.x - i.x) ** 2 + (center.y - i.y) ** 2
			if mxdist < dist:
				mxPoint = i
				mxdist = dist		
		center.x = center.x + (mxPoint.x - center.x) * w
		center.y = center.y + (mxPoint.y - center.y) * w
		w *= 0.9995 # 학습률 감소시킴
	
	# Output the result with high precision
	print(f"{format_float(center.x)} {format_float(center.y)}")
	print(f"{math.sqrt(mxdist):.3f}")

if __name__ == "__main__":
	main()