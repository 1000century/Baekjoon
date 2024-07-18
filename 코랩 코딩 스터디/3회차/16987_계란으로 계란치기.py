# (세현)
"""
<시간줄이는 방법 2가지>
deepcopy 쓰면 시간초과 끔. 귀찮아도 백트래킹 원래하듯 원상복구 시켜야함.
깨진 개란개수 셀 때 함수 인자로 넣어두지 않고 매번 체크하는 걸로 하면 시간초과

cf) setrecursionlimit은 안해도 됨
"""

import sys
ans = 0
input = sys.stdin.readline
def solution(eggs,idx,broken):
	global ans

	# 종료조건 2가지
	if idx==len(eggs):
		ans = max(ans,broken)
		return
	if broken == len(eggs)-1:
		ans = max(ans,broken)
		return

	# 다음 인덱스로 넘어가는 조건 1가지
	if eggs[idx][0]<=0:
		solution(eggs,idx+1,broken)
		return
	
	# DFS 수행
	for i in range(len(eggs)):
		if i == idx:
			continue
		if eggs[i][0]<=0:
			continue
		eggs[i][0] = eggs[i][0]-eggs[idx][1]
		eggs[idx][0] = eggs[idx][0]-eggs[i][1]
		solution(eggs,idx+1,broken + (eggs[i][0]<=0)+(eggs[idx][0]<=0))
		eggs[i][0] = eggs[i][0]+eggs[idx][1]
		eggs[idx][0] = eggs[idx][0]+eggs[i][1]

N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]
solution(eggs,0,0)
print(ans)


