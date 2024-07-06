import sys
from collections import deque
que = deque([])

N = int(sys.stdin.readline().strip())
for _ in range(N):
    A = list(sys.stdin.readline().strip().split())
    cmd = int(A[0])

    if cmd ==1:
        a = int(A[1])
        que.appendleft(a)
    elif cmd == 2:
        a = int(A[1])
        que.append(a)
    elif cmd == 5:
        print(len(que))
    elif cmd == 6:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(que) == 0:
            print(-1)
        else:
            if cmd == 3:
                b = que[0]
                print(b)
                que.popleft()
            elif cmd == 4:
                b = que[-1]
                print(b)
                que.pop()
            elif cmd == 7:
                b = que[0]
                print(b)
            elif cmd == 8:
                b = que[-1]
                print(b)
