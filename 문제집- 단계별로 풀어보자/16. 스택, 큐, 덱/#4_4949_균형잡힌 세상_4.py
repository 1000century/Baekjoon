symbol = ["[", "]", "(", ")"]
while True:
    S = input()
    if S == ".":
        exit()
    new = ""
    for _ in S:
        if _ in symbol:
            new = new + _
    while True:
        if "[]" in new:
            new = new.replace("[]", "")
        elif "()" in new:
            new = new.replace("()","")
        else:
            break
    if new =="":
        print("yes")
    else:
        print("no")
