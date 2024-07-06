from collections import deque
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
B = list(map(int,sys.stdin.readline().strip().split()))
B = deque(B)
M = int(sys.stdin.readline().strip())
C_rough = input().split()
C = []
for _ in C_rough:
    C.append(int(_))

for element in C:
    if A[0] == 1:
        next = element
        B.append(B[0])
        B.popleft()
    else:
        next = B[0]
        B.append(element)
        B.popleft()


    for i in range(1,N):
        if A[i] ==1:
            next = next
            B.append(B[0])
            B.popleft()
        else:

            B.append(next)
            next = B[0]
            B.popleft()
    print(next)
