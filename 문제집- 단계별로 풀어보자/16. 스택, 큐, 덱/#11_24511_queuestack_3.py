from collections import deque
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
B = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
C_rough = sys.stdin.readline().strip().split()
C = []
for _ in C_rough:
    C.append(int(_))
next = C[0]
for element in C:
    for i in range(0,N):
        if A[i] !=1:
            temp = next
            next = B[i]
            B[i] = temp
    print(next, end= " ")
