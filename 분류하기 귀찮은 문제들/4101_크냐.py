while True:
    response = input()
    if response == "0 0":
        break
    else:

        a, b = map(int,response.split())
        if a> b:
            print("Yes")
        else:
            print("No")

