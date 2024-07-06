from collections import deque

N, K = map(int,input().split())
que = deque([])
for i in range(1,N+1):
    que.append(i)

print("<",end="")
for _ in range(N-1):
    for kk in range(K-1):
        a =que[0]
        que.popleft()
        que.append(a)
    a3 = que[0]
    que.popleft()
    print(a3,end=", ")
print(que[0],end=">")

