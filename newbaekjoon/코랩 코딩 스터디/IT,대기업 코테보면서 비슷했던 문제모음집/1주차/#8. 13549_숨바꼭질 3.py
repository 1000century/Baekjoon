# (세현)

import heapq

N,K = map(int,input().split())
q = []
dp=[int(1e9)]*(100001)

dp[N] = 0
heapq.heappush(q,(0,N))

while q:
	time, now = heapq.heappop(q)
	if now ==K:
		print(time)
		break

	next = now+1
	if 0<=next<100001:
		if dp[next] > time + 1:
			dp[next] = time + 1
			heapq.heappush(q,(time+1,next))

	next = now -1
	if 0<=next<100001:
		if dp[next] > time + 1:
			dp[next] = time + 1
			heapq.heappush(q,(time+1,next))

	next = now*2
	if 0<=next<100001:
		if dp[next] > time:
			dp[next] = time
			heapq.heappush(q,(time,next))

