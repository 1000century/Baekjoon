N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))
B = sorted(B)
for _ in range(N):
    print(B[_])
