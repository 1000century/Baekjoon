import sys

T = int(input())

for _ in range(T):
    a = sys.stdin.readline().rstrip().split(" ")
    a = [int(x) for x in a]
    print(sum(a))

