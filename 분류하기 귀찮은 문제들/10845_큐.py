import sys
from queue import Queue
N = int(sys.stdin.readline().strip())
que = Queue()


for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[1] == "u":
        que.put(int(cmd[5:]))
    elif cmd =="size":
        print(que.qsize())
    elif cmd == "empty":
        if que.empty() == True:
            print(1)
        else:
            print(0)
    else:
        if que.qsize() == 0:
            print(-1)
        else:
            if cmd == "pop":
                print(que.queue[0])
                que.get()
            elif cmd == "front":
                print(que.queue[0])
            elif cmd == "back":
                print(que.queue[-1])