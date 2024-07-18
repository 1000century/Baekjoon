import sys
N = int(input())
M = []
for _ in range (N):
    M.append(int(sys.stdin.readline().strip()))
M = sorted(M)
for _ in range(N):
    print(M[_])
