import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
    sentence = sys.stdin.readline().strip().split()
    for i in sentence:
        print(i[::-1], end = " ")
    print()
