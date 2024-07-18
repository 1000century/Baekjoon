while True:
    N = int(input())
    if N == -1:
        break
    else:

        a = int(N ** (0.5))
        group = []
        for _ in range(1, a + 1):
            if N % _ == 0:
                group.append(_)
                group.append(N // _)
        group = list(set(group))
        group.sort()
        sum = 0
        for _ in group:
            sum = sum + _
        if sum-N == N:
            groups = []
            for _ in range(len(group)-1):
                groups.append(group[_])
            str(groups)
            letter =" + ".join(str(_) for _ in groups)
            print(N," = ",letter,sep="")
        else:
            print(N, "is NOT perfect.")