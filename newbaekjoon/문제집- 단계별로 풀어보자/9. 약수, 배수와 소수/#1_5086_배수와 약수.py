while True:
    response = input()
    if response == "0 0":
        break
    else:
        a, b = map(int,response.split())
        if b % a == 0:
            print("factor")
        elif a % b ==0:
            print("multiple")
        else:
            print("neither")

