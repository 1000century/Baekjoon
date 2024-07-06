import sys

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())

B = list(map(int,sys.stdin.readline().strip().split()))
A = sorted(A)

m = int(N/2)
for b in B:
    if b < A[0] or b>A[-1]:
        print(0)
    else:
        isitin = 0
        if b <= A[m]:
            i = 0
            while b <= A[m] and i <= m:
                if b != A[i]:
                    i = i+1
                else:
                    isitin = 1
                    break
        else:
            i = m + 1
            while b > A[m] and i <= N-1:
                if b != A[i]:
                    i = i + 1
                else:
                    isitin = 1
                    break
        print(isitin)




