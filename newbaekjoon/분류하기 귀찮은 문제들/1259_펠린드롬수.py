while True:
    N = input()
    if N == "0":
        exit()
    else:
        count = 0
        for _ in range(len(N)):
            if N[_] != N[len(N)-1-_]:
                count = count +1
        if count ==0:
            print("yes")
        else:
            print("no")