# (세현)

import sys
from collections import Counter
input = sys.stdin.readline
N,H = map(int,input().split())

아래,위 =  [],[]
for i in range(N):
	if i %2 == 0:아래.append(int(input()))
	else:		 위.append(int(input()))

def solve(arr):
	ans = [0]*(H+1)
	for idx,i in Counter(arr).items():
		ans[idx] = i
	for i in range(max(arr)-1,0,-1):
		ans[i] = ans[i+1]+ans[i]
	return ans[1:]

아래ans,위ans = solve(아래),solve(위)
ans = list(위ans[i]+아래ans[-1-i] for i in range(H))

print(min(ans),ans.count(min(ans)))