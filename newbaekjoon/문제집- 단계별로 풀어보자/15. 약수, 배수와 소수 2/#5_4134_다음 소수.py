N = int(input())
for _ in range(N):
    plus = 0
    ori = int(input())
    if ori == 0 or ori == 1 or ori == 2:
        print(2)
    else:
        ori_odd = int(ori//2) * 2 + 1
        ori_print = ori_odd
        divider = 3
        while divider <= int(ori_print ** 0.5):
            if ori_print % divider != 0:
                divider = divider + 2
            else:
                ori_print = ori_print + 2
                divider = 3
        print(ori_print)
