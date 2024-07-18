import sys
T = int(input())
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split())
    m = min(a,b)
    for i in range(m,0, -1):
        if a % i == 0 and b % i == 0:
            break
    print(a * b // i)
