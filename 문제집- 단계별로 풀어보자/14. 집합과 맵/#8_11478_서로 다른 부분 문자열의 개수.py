import sys
N = sys.stdin.readline().strip()
c = len(N)
A = []
for _ in range(c):
    for i in range(c-_+1):
        A.append(N[i:i+_])

A_1 = list(set(A))
print(len(A_1))