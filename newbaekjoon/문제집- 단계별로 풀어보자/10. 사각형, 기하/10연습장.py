N = int(input())
A = {}
for _ in range(N):
    x = input()
    length = len(x)
    num = 0
    for p in range(length):
        num = num + (ord(x[p]) - 96) * (30 ** (length - 1 - p))

    A[x] = num

A = sorted(A.items(), key=lambda x: x[-1])
for _ in range(len(A)):
    print(A[_][0])

