# 시도 1) N-1
# 시도 2) 이렇게 저렇게 해봤는데 뭔 문제인지 모르겠음
### 그리고 간선 전체를 하나의 리스트로 만들고 그 다음에 union-find 시행해야함.

import sys
input = sys.stdin.readline

T = int(input())

def travel():
	N,M = map(int,input().split())
	parent = {}
	for i in range(1,N+1):
		parent[i] = i
	X = []
	for _ in range(M):
		temp = list(map(int,input().split()))
		temp.sort()
		X.append(temp)
	X.sort()
	for a,b in X:
		union(a,b,parent)
	
	count = 0
	for i in range(1,N+1):
		count = count + 1
	print(count-1)



def find(x,parent):
	if x != parent[x]:
		parent[x] = find(parent[x],parent)
	return parent[x]

def union(a,b,parent):
	a = find(a,parent)
	b = find(b,parent)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

for _ in range(T):
	travel()


