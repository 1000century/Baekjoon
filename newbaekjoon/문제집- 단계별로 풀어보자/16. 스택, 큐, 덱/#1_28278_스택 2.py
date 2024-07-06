import sys
Stack = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    A = sys.stdin.readline().strip()
    if len(A)>1:
        X = int(A[2:])
        Stack.append(X)
    else:
        B = int(A)
        if B==3 or B==4:
            result = len(Stack)*(4-B)+(B-3)*int(1-(len(Stack)/(len(Stack)+1)))
            print(result)
        else:
            if len(Stack) == 0:
                print(-1)
            else:
                if B == 2:
                    print(Stack[-1])
                    Stack.pop()
                if B == 5:
                    print(Stack[-1])


