import sys
N = int(input())

check_list = [0] *10001
for _ in range(N):
    a = int(sys.stdin.readline())
    check_list[a] = check_list[a] + 1
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)