"""
24.03.28
함수로 바꿨을 뿐인데 4300ms > 2220ms
"""

N,M = map(int,input().split())
X = list(map(int,input().split()))

def treecut(M):
	st = 0
	en = 1000000000
	while st<=en:
		mid = (st + en)//2

		wood = 0
		for tree in X:
			if tree>mid:
				wood = wood + (tree-mid)
		
		if wood >= M: # 설정한 나무가 너무 낮아서 너무 많이 나무를 잘랐다면
			st = mid + 1
		else: #upperbound
			en = mid - 1

	print(st-1)
treecut(M)