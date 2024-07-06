# (세현)

while True:
    T = input()
    a,b,c = map(int,T.split())
    S = [a,b,c]
    if T == "0 0 0":
        break
    elif a+b-c <=0 or b+c-a<=0 or c+a-b<=0:
        print("Invalid")
    else:
        if len(list(set(S))) ==1:
            print("Equilateral")
        elif len(list(set(S))) ==2:
            print("Isosceles")
        else:
            print("Scalene")

