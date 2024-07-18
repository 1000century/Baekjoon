N, K = map(int,input().split())

M =1
for _ in range(K):
    M = M * (N-_)
for _ in range(K):
    M = M // (K-_)
print(int(M))