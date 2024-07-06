while True:
    S = input()
    if S == ".":
        exit()
    result = "yes"
    S = list(S)
    a = 0
    b = 0
    symbol = ["[","]","(",")"]
    delta_a = 0
    delta_b = 0
    for element in S:
        if element in symbol:
            value = 2 * symbol.index(element)
            delta_a_prev = delta_a
            delta_b_prev = delta_b
            delta_a = ((value - 4) // 4) * (-1) * ((value - 1))
            delta_b = (value // 4) * (value - 5)
            a = a + delta_a
            b = b + delta_b
            print(element, value)
        else:
            continue

        if a >0 or b>0:
            result = "no"
            break
        elif delta_a * delta_b_prev < 0:
            break
        elif delta_b * delta_a_prev < 0:
            break
    print(result, a, b)