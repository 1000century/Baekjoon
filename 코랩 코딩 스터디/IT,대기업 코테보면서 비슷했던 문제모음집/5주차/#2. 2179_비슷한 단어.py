# 시도 1) pypy로만 통과 3600ms

import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = set()
for _ in range(N):
	words.add(input().rstrip())
words = list(words)

ans = [0,"",""]
for i in range(len(words)):
	x = words[i]
	for j in range(i+1,len(words)):
		y = words[j]
		cnt = 0
		for k in range(len(x)):
			if len(y)>=k+1:
				if x[k] != y[k]:
					break
				cnt = cnt + 1
		if cnt > ans[0]:
			ans = [cnt,x,y]
print(ans[1])
print(ans[2])


