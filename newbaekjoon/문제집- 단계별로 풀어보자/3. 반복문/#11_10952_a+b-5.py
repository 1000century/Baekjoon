for i in range(1,10000):
    a = input().split()
    if a ==["0", "0"]:
        break
    else:
        a= [int(x) for x in a]
        print(sum(a))