N = int(input())
A = []

for _ in range(N):
    x, y = map(int,input().split())
    A.append([y,x])

A = sorted(A)
for _ in range(len(A)):
    print(A[_][1],A[_][0],sep=" ")