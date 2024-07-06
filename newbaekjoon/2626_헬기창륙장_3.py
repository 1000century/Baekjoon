import os

def get_output_file_path():
    script_name = os.path.basename(__file__)  # 현재 파일의 이름을 가져옴
    base_name, _ = os.path.splitext(script_name)  # 확장자를 제거
    output_path = rf'C:\Users\Sese\baekjun\output\{base_name}_output.txt'
    # 파일 생성
    with open(output_path, 'w') as file:
        pass  # 파일을 열고 바로 닫아서 빈 파일을 생성합니다.
    return output_path

def save_data_to_file(data, filename):
    with open(filename, 'a') as file:
        file.write(data + '\n')


import math

def format_float(val):
	formatted = f"{val:.3f}"
	if formatted == "-0.0000":
		return "0.0000"
	return formatted


def main():
	output_file = get_output_file_path()
	N = int(input())
	fan = []
	for _ in range(N):
		a, b = map(int, input().split())
		fan.append([a, b])
	
	w = 0.1
	center = [0,0]
	
	# Calculate initial center of all points
	for i in fan:
		center[0] += i[0] / N
		center[1] += i[1] / N
	
	# Iteratively adjust center towards the furthest point
	mxdist, radius = 0, 0
	for _ in range(23000):
		mxdist = 0
		mxPoint = None
		for i in fan:
			dist = (center[0] - i[0]) ** 2 + (center[1] - i[1]) ** 2
			if mxdist < dist:
				mxPoint = i
				mxdist = dist
		
		# Adjust center towards the furthest point
		center[0] += (mxPoint[0] - center[0]) * w
		center[1] += (mxPoint[1] - center[1]) * w
		save_data_to_file(f"Learning Rate: {w}",output_file)
		w *= 0.994
	
	# Output the result with high precision
	print(f"{format_float(center[0])} {format_float(center[1])}")
	print(f"{math.sqrt(mxdist):.3f}")


if __name__ == "__main__":
	main()