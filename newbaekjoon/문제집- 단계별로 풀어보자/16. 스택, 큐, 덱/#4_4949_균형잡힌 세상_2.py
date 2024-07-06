while True:
    S = input()
    if S == ".":
        exit()
    S = list(S)
    dict = {
        "[":   1,
        "]" : -1,
        "(" :  2,
        ")" : -2
    }
    result = 0
    for i in range(len(S)):
        value = dict.get(S[i])
        if value == None:
            value = 0
        if value <0 :
            result = result + value
        elif value >0:
            result = result * 10 + value

        if result % 10 >2 and value !=0:
            final_print = "no"
            break
        elif result % 10 == 0 and result != 0 and value != 0:
            result = result // 10
        print(result, end=" ")

    if result == 0:
        final_print = "yes"
    if result !=0 and final_print!="no":
        final_result = "no"
    print("결과는",result,final_print)