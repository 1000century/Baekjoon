import sys

stack= []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[1] =="u":
        A, X = cmd.split()
        stack.append(int(X))
    elif cmd[0] == "s":
        print(len(stack))
    elif cmd[0] == "e":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            if cmd == "pop":
                print(stack[0])
                stack.pop(0)
            elif cmd == "front":
                print(stack[0])
            else:
                print(stack[-1])