import sys
from collections import deque
N = int(sys.stdin.readline().strip())
deq = deque()

for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[1] == "u":
        if cmd[5] == "f":
            deq.appendleft(int(cmd[11:]))
        elif cmd[5] == "b":
            deq.append(int(cmd[10:]))
    elif cmd =="size":
        print(len(deq))
    elif cmd == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(deq) == 0:
            print(-1)
        else:
            if cmd == "pop_front":
                print(deq[0])
                deq.popleft()
            elif cmd == "pop_back":
                print(deq[-1])
                deq.pop()
            elif cmd == "front":
                print(deq[0])
            elif cmd == "back":
                print(deq[-1])