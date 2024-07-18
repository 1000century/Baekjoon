N = int(input())
for K in range(1,N+1):
    M = K
    a = M
    while M != 0:
        a = a + M % 10
        trash = (M //10) % 10
        M = M // 10
    if a + trash   == N:
        print(K)
        exit()
print(0)