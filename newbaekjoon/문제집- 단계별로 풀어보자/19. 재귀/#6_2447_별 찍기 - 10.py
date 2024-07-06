
def ff(n):
    if n ==1:
        return ["***"]
    else:
        unit = star(n-1)
        a1 = unit[0][0]*3
        a2 = unit[1][0]*3
        a3 = unit[2][0]*3
        united = [a1,a2,a3]
        print("ff",united)

        return united
def sf(n):
    if n ==1:
        return ["* *"]
    else:
        unit = star(n-1)
        blank = " "*(3**(n-1))
        a1 = unit[0][0]*3
        a2 = unit[1][0] + blank + unit[1][0]
        a3 = a1
        united = [a1,a2,a3]
        print("sf",united)

        return united



def star(n):
    sq = []
    if n == 1:
        sq.append(ff(1))
        sq.append(sf(1))
        sq.append(ff(1))
        return sq
    else:
        sq.append(ff(n))
        sq.append(sf(n))
        sq.append(sq[0])
        return sq

results = star(1)
print(results)

result = star(2)
print(result)

resul = star(3)
print(resul)
