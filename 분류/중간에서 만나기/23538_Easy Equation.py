# 브루트포스 5,4,3 까지만 브루트포스하고 그다음엔 squar root로 계산
# >> 이건 pypy로만 통과됨
import math

def main():
	n = int(input())
	answer = 0
	x = 1
	while x**5 < n:
		y = 1
		while x**5 + y**4 < n:
			z = 1
			while x**5 + y**4 + z**3 < n:
				m = n - x**5 - y**4 - z**3
				d = int(math.sqrt(m - 1))
				answer += d
				z += 1
			y += 1
		x += 1
	print(answer)

if __name__ == "__main__":
	main()
