import sys
N = int(sys.stdin.readline().strip())
A = ["ChongChong"]
start  = 0
for _ in range(N):
    peo = sys.stdin.readline() .strip().split()
    if "ChongChong" in peo:
        start = 1
    if start == 1:
        if peo[1] in A or peo[0] in A:
            A.append(peo[1])
            A.append(peo[0])
            A = list(set(A))
print(len(A))
