N = int(input())
A = []

for _ in range(N):
    x, y = map(int,input().split())
    A.append((x,y))

A = sorted(A)
for _ in range(len(A)):
    print(A[_])