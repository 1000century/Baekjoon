from queue import Queue
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
B = list(map(int,sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
C_rough = input().split()
C = []

for _ in C_rough:
    C.append(int(_))

for element in C:
    que = Queue()
    if A[0] == 1:
        next = element
        que.put(B[0])
    else:
        next = B[0]
        que.put(element)
    for i in range(1,N):
        if A[i] ==1:
            next = next
            que.put(B[i])
        else:
            que.put(next)
            next = B[i]
    B = list(que.queue)
    print(next, end =" ")

