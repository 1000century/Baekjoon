# (세현)
# 자료구조 -스택
# 탑(BOJ 2493반)과 거의 비슷한 문제

import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []

for i in range(n):
	x, h = map(int,input().split())

	# Part 1. 건물개수 카운트
	# 이번 높이가 직전 건물 높이보다 낮은 경우에만 카운트
	while stack and stack[-1]>h:
		count = count + 1
		stack.pop()
	
	# Part 2. stack에 추가
	# 이번 높이가 0 이 아니면서 + 직전 건물높이보다 큰 경우에만 추가
	if h != 0:
		if not stack or stack[-1] < h : # 직전 건물높이랑 같으면 추가 안해줌.
			stack.append(h)

# Part 3. 마지막 건물 높이가 0으로 끝나지 않은 경우
# stack에 남아있는 높이만큼 건물 개수 추가해줌
count = count + len(stack)
print(count)