# (세현)
"""
1. 43%에서 틀림 >> ans_height이 0m일 수도 있음
반례)
1 1
1
answer : 0
2. X.sort()하든 안하든 시간 똑같음 2252ms > 2252ms
3. def으로 안하면 시간초과 뜸
"""

N,M = map(int,input().split()) #N 나무의 수, M 나무의 길이
X = list(map(int,input().split()))

X.sort(reverse=True)

def binary(X, M):
	start = 0
	end = 2000000001
	ans_height = 0
#	print(start,end,height)

	while start < end:
		height = (start + end) // 2
		result = 0
		for tree in X:
			if tree > height:
				result = result + (tree-height)
			else:
				break

		if result >= M: # 너무 많이 잘랐다면 height를 높여야 함
#			print(height)
			ans_height = max(ans_height,height) # 우선 정답 먼저 출력해두고
			start = height+1 # 딱 height은 포함 안해도 됨

		else:
			end = height # 딱 height은 포함 안해줘도 됨
#		print(start,end,height)

	print(ans_height)

binary(X,M)

	