while True:
    S = input()
    if S == ".":
        exit()
    S = list(S)
    dict = {"[":   [1, 0], "]" : [-1,0], "(" : [0, 1], ")" : [0, -1]}
    result = [0,0,None]
    fin_print = "yes"
    ## switch 개념
    for i in range(len(S)):
        value = dict.get(S[i])
        if value == None:
            continue
        else:
            sumandb = value[0] + value[1]
            result[0] = result[0] + value[0]
            result[1] = result[1] + value[1]
            if result[2] == None:
                result[2] =  1-value.index(0)
            if sumandb < 0 and result[2] != 1-value.index(0):
                fin_print = "no"
                result[2] = 1-value.index(0)
                print(result, end=" ")
                break
            result[2] = 1 - value.index(0)
            print(result,"@@",end=" ")
        if result[0] < 0 or result[1]< 0:
            fin_print = "no"
            break
    if fin_print =="no":
        print(fin_print,result)
    else:
        if result[0] ==0 and result[1] == 0:
            print(fin_print,result)
        else:
            print("no",result,"@@")