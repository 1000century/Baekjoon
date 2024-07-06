import sys
N = int(sys.stdin.readline().strip())
stack = []


for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[1] == "u":
        stack.append(int(cmd[5:]))
    elif cmd =="size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            if cmd == "pop":
                print(stack[-1])
                stack.pop()
            elif cmd == "top":
                print(stack[-1])
