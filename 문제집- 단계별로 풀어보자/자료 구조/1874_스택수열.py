import sys
n = int(sys.stdin.readline().strip())
A = []
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a in A:
        print("-")
    else:
        print("+")
        