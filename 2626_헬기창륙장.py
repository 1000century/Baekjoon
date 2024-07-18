import math

# Fast input setup for competitive programming is not needed in Python due to its interpreted nature.
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
	
	# Calculate initial center of all points
	for i in fan:
		center.x += i.x / N
		center.y += i.y / N
	
	# Iteratively adjust center towards the furthest point
	mxdist, radius = 0, 0
	for _ in range(100000):
		mxdist = 0
		mxPoint = None
		for i in fan:
			dist = (center.x - i.x) ** 2 + (center.y - i.y) ** 2
			if mxdist < dist:
				mxPoint = i
				mxdist = dist
		
		# Adjust center towards the furthest point
		center.x = center.x + (mxPoint.x - center.x) * w
		center.y = center.y + (mxPoint.y - center.y) * w
		w *= 0.9995 # 학습률 감소시킴
	
	# Output the result with high precision
	print(f"{format_float(center.x)} {format_float(center.y)}")
	print(f"{math.sqrt(mxdist):.3f}")

if __name__ == "__main__":
	main()