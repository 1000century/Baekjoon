N = int(input())
if N == 1:
    print("")
else:
    M = N
    for _ in range(2,N+1):
        while M % _ == 0 :
            if M % _ == 0:
                print(_)
                M = M // _