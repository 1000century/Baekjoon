#3 9012  괄호
N = int(input())
for _ in range(N):
    PS = list(input())
    check = 0
    for element in PS:
        if element == "(":
            check = check + 1
        else:
            check = check - 1
        if check == -1:
            print("NO")
            break
    if check == 0:
        print("YES")
    elif check > 0:
        print("NO")
