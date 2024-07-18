while True:
    N = int(input())
    if N == 0:
        break
    A = {}
    for _ in range(N):
        x = input()
        length = len(x)
        num = 0
        for p in range(length):
            print("x[",p,"] = ", (ord(x[p]) - 96), length-1-p)
            num = num + (ord(x[p]) - 96) * (30 ** (length - 1 - p))

        A[x] = num

    A = sorted(A.items(), key=lambda x: x[1])
    print(A)
    for _ in range(len(A)):
        print(A[_][0])

