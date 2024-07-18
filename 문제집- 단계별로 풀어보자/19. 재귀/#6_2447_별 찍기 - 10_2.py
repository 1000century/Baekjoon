
def ff(n):
    if n ==1:
        return "***"
    else:
        unit = star(n-1)
        united = []
        for _ in range(len(unit)):
            united.append(unit[_]*3)

        return united
def sf(n):
    if n ==1:
        return "* *"
    else:
        unit = star(n-1)
        united = []
        blank = " "*(3**(n-1))
        for _ in range(len(unit)):
            united.append(unit[_]+blank+unit[_])
        return united

def star(n):
    sq = []
    if n == 1:
        sq.append(ff(1))
        sq.append(sf(1))
        sq.append(ff(1))
        return sq
    else:
        temp =[]
        temp.append(ff(n))
        for ele in temp[0]:
            sq.append(ele)

        temp = []
        temp.append(sf(n))
        for ele in temp[0]:
            sq.append(ele)

        temp =[]
        temp.append(ff(n))
        for ele in temp[0]:
            sq.append(ele)
        return sq


import sys
N = int(sys.stdin.readline().strip())
for i in range(1,12):
    if 3**i == N:
        n = i
        break

result = star(n)
for i in result:
    print(i)