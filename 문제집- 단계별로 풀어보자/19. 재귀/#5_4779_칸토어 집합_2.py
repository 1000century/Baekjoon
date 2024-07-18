def Kant_div(A,dis):

    d = dis
    d_3 = d // 3
    if d == 1:
        return["-"]
    elif d == 3:
        return ["-"," ", "-"]
    else:
        A1 = Kant_div(A[:d_3],d_3)
        A2 = [" "] * d_3
        A3 = Kant_div(A[-1-d_3+1:],d_3)
        return A1+A2+A3
while True:
    try:

        line = input()
        N = int(line.strip())  # 각 줄에서 정수 N을 추출합니다

        n = 3 ** N
        A = ["-"] * n

        result = Kant_div(A, n)

        for x in result:
            print(x, end="")
        print()
    except EOFError:
        break