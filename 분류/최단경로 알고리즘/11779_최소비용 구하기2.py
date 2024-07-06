# 시도 1. 지나온 도시는 거꾸로 찾지 않아서 시간초과 생김
# 시도 2. if ways[v] < cost: continue    <<< 이 부분 빠져서 시간초과
# 시도 3. 다 고치니까 풀림

import heapq
from collections import deque
import sys
input = sys.stdin.readline

# Part 1. 기본적인 입력
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
	a,b,c = map(int,input().split())
	graph[a].append([b,c])

st, en = map(int,input().split())



# Part 2. 다익스트라 + 지나온 길 찾기
X = []
heapq.heappush(X,(0,st))
ways = [int(1e9)]*(N+1)
ways[st] = 0
passedcity = [0]*(N+1) # 방금 전 지나온 도시가 몇 번이었는지


# Part 2a. 다익스트라
while X:
	cost,v= heapq.heappop(X)
	if ways[v] < cost:
		continue # 이 부분이 없으면 들어온 모든 간선에 대해서 처리하기 때문에 시간초과
	for nv,extradist in graph[v]:
		ncost = cost + extradist
		if ncost < ways[nv]:
			heapq.heappush(X,(ncost,nv))
			passedcity[nv] = v # 지나온 도시를 거꾸로 저장
			ways[nv] = ncost


# Part 2b. 지나온 길 찾기
q = deque([en])
sequence = []
while q:
	v = q.popleft()
	sequence.append(v)
	if v == st:
		break
	bv = passedcity[v] # bv: before city
	q.append(bv)



# Part 3. 정답 출력
print(ways[en])
print(len(sequence))
print(*sequence[::-1])