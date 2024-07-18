S = list(input())
dict = {}
for i in S:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
dict.sor

sorted = sorted(dict.items(), key=lambda x)

sorted_2 = sorted(dict.items(),key=lambda x: (-x[1][1], -x[1][0],x[0]))
