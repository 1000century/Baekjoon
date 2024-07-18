from collections import deque
que = deque([])

N = int(input())

for i in range(1,N+1):
    que.append(i)

for _ in range(N-1):
    que.popleft()
    sec = que[0]
    que.append(sec)
    que.popleft()

print(que[-1])