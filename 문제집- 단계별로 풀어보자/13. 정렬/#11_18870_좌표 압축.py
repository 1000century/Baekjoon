N = int(input())
Y = list(map(int,input().split()))
b = 0
a = 0
for _ in range(N):
    Min = min(Y)
    Max = max(Y)
    if _ == 0:

        a = Y.index(Min)
        b = a
        Y[a] = 10000000000+_+Min
    elif _ == N-1:

        b = a
        a = Y.index(Min)
        if Max != 10000000000+_+Min-1:
            Y[b] = 10000000000+_-1
            Y[a] = 10000000000+_
        else:
            Y[b] = 10000000000+_-1
            Y[a] = 10000000000+_-1
    else:

        b = a
        a = Y.index(Min)
        if Max != 10000000000+_+Min-1:
            Y[b] = 10000000000+_-1
            Y[a] = 10000000000+_+Min
        else:
            Y[b] = 10000000000+_-1
            Y[a] = 10000000000+_+Min -1

result = [x - 10000000000 for x in Y]
print(*result, sep=" ")

