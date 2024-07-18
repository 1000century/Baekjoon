# (세현)

# 시도 1) pypy로만 통과 3600ms
# 시도 2) 아이디어: 첫글자가 같은 애들을 하나의 리스트로 만들어서 그 안끼리 비교함.
"""
전반적으로 핵심이 되는 아이디어
	>>>> 애초에 지금까지의 접두사 최대길이보다 단어의 길이가 작은 경우 pass
	ex) 현재까지 비교한 두 단어의 접두사 최대길이가 4라고 할 때\
		만약 비교대상이 되는 단어가 "war"같이 3글자라면 used에 넣어버려서 탐색을 하지 않음.



Part 1. 첫글자가 같은 애들을 temp에 넣기
	- 단어들의 리스트를 이중 for문으로 첫글자 같은 애들을 묶음.
	첫번째 for문의 단어:x, 두번째 for문의 단어:y

	Part 2. 첫글자가 같은 애들이 모인 temp에서 단어들을 비교
	- temp에 들어있는 단어들을 비교(이중 for문)
		(첫번째 for문의 단어: p, 두번째 for문의 단어: q)
		1) p가 지금까지의 접두사 최대길이보다 작으면 pass (이걸로 속도 엄청나게 단축됨)
		2) q가 지금까지의 접두사 최대길이보다 작거나
		3) p와 q의 (지금까지의 접두사 최대길이)인덱스가 다르면 continue

"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = []
for _ in range(N):
	words.append(input().rstrip())

ans = [0,"",""]

# Part 1 첫글자가 같은 애들을 temp에 넣기
# 각 x별로 첫글자가 같은 애들을 temp로 넣고 그 temp에 들어있는 애들끼리 최대치 비교
used = set() # used에 한번 들어간 순간 다시 탐색될 가능성 없음(탐색시간 단축)
for x in words:
	if x in used:
		continue
	temp = [x]
	used.add(x)
	if len(x) <ans[0]: # ans[0]: 지금까지의 접두사 최대길이
		continue
	for y in words:
		if y in used:
			continue
		if len(y) < ans[0]: # ans[0]: 지금까지의 접두사 최대길이
			continue
		if x[0] == y[0]:
			used.add(y)
			temp.append(y)
			if ans[0] ==0:
				ans = [1,x,y]
	
	# Part 2. temp에 들어있는 애들끼리의 비교(이중포문)
	# 첫번쩨 for문의 단어: p, 두번째 for문의 단어 :q
	for i in range(len(temp)):
		p = temp[i]
		# 1) p가 지금까지의 접두사 최대길이보다 작으면 pass (이걸로 속도 엄청나게 단축됨)
		if len(p) < ans[0]:
			continue
		for j in range(i+1,len(temp)):
			q = temp[j]
			cnt = 1
			# 2) q가 지금까지의 접두사 최대길이보다 작거나
			if len(q)<ans[0]:
				continue
			# 3) p와 q의 (지금까지의 접두사 최대길이)인덱스가 다르면 continue
			if p[ans[0]-1] != q[ans[0]-1]:
				continue
			for k in range(1,len(p)):
				if len(q) >= k+1:
					if p[k] != q[k]:
						break
					cnt = cnt + 1
			if cnt > ans[0]:
				ans = [cnt,p,q]
print(ans[1])
print(ans[2])