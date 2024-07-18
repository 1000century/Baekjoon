from collections import deque

def solution(stones, k):
	answer = int(1e9)*9
	n = len(stones)
	q = deque([])
	for i in range(n):
		while q and q[-1][1] <= stones[i]:
			q.pop()
		if q and (q[0][0]+k) < i+1:
			q.popleft()
		q.append([i,stones[i]])
		if i>=k-1:
			answer = min(answer,q[0][1])
	return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([7, 2, 8, 7, 2, 5, 9], 3))
print(solution([1, 2, 1, 2, 1], 2))
