"""
24.03.12
수학적으로 풀기 실패
22%에서 틀렸습니다.
"""
import sys
N,M,B = map(int,sys.stdin.readline().split())
A= []
S = {}
for _ in range(N):
	X = list(map(int,sys.stdin.readline().split()))
	for element in X:
		if element in S:
			S[element] += 1
		else:
			S[element] =1

#print("그원소, 개수, 원소합",S)

def how_time_blocks(S,B):
	ans_height = 0
	ans_time=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
	for h in range (0,257):
		time = 0
		blocks = B
		for key,value in S.items():
			if key > h: # 쌓여진 높이가 목표보다 더 높으면 제거해야 함
				time = time + 2* (key-h)*value # 2초
				blocks = blocks + (key-h)*value # 제거해서 쌓여진 블록 개수
			if key < h: # 쌓여진 높이가 목표보다 더 낮으면 더 추가해야 함
				time = time + (h-key)*value # 1초
				blocks = blocks - (h-key)*value
		if blocks < 0 or time > ans_time:
			break
		else:
			ans_height = h
			ans_time = time
#		print("h", h, "time", time, "남은 블럭수",blocks)
	print(ans_time, ans_height)
		
how_time_blocks(S,B)

