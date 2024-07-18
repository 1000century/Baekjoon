from collections import deque
import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
    I = deque()
    N,M = map(int,sys.stdin.readline().strip().split())
    I.extend(list(map(int,sys.stdin.readline().strip().split())))
    i = 0
    count = 1
    while True:
        if I[0] != max(I):
            I.append(I[0])
            I.popleft()
            if M == 0:
                M = len(I)
        else:
            I.popleft()
            if M == 0:
                print(count)
                break
            count = count + 1
        M = M -1