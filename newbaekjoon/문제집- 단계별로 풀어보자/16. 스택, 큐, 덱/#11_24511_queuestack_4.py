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
for i in range(0,N)[::-1]:
    if A[i] ==1:
        del B[i]
D = []

for i in range(len(B) - 1, -1, -1):
    D.append(B[i])
for item in C:
    D.append(item)
for _ in range(len(C)):
    print(D[_], end=' ')