N = int(input())
count = 0
for _ in range(66600000):
    A = str(_)
    B = list(A)
    if "666" in A and B.count("6")>2:
        count = count+1
    if N == count:
        print(_)
        break