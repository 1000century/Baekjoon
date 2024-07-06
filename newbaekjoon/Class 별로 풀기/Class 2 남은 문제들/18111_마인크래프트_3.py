"""
24.03.12
수학적으로 풀기 실패
22%에서 틀렸습니다.
"""
N,M,B = map(int,input().split())
A= []
S = []
hap = 0
for _ in range(N):
	X = list(map(int,input().split()))
	A.extend(X)
A.sort()

S.append([A[0],0]) # 딱 그 원소 합, 개수
before = A[0]
for i in range(len(A)):

	now= A[i]
	if now == before:
		S[-1][1] = S[-1][1] + 1
	else: # now< before
		S.append([now,1])
	before = S[-1][0]
#print("그원소, 개수, 원소합",S)

def how_time_blocks(S,h,B):
	global ans_height, ans_time
	time = 0
	blocks = B
	for s in S:
		if s[0] > h: # 쌓여진 높이가 목표보다 더 높으면 제거해야 함
			time = time + 2* (s[0]-h)*s[1] # 2초
			blocks = blocks + (s[0]-h)*s[1] # 제거해서 쌓여진 블록 개수
		if s[0] < h: # 쌓여진 높이가 목표보다 더 낮으면 더 추가해야 함
			time = time + (h-s[0])*s[1] # 1초
			blocks = blocks - (h-s[0])*s[1]
	if blocks < 0:
		print(ans_time, ans_height)
		exit()
	if time<=ans_time:
		ans_height = h
		ans_time = time
#	print("h", h, "time", time, "남은 블럭수",blocks)
		
ans_height = 0
ans_time=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for h in range(0,257):
	how_time_blocks(S,h,B)
print(ans_time, ans_height)

