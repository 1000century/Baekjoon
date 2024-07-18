import sys
n = int(input())
entry = {}
for _ in range(n):
    p,c = sys.stdin.readline().split()
    if c == "enter":
        entry[p] = 1
    else:
        entry[p] = 0
G =[]
for _ in entry:
    if entry[_] == 1:
        G.append(_)
G_1 = sorted(G)
for _ in range(len(G_1)):
    print(G_1[len(G_1)-1-_])

"""
이렇게 하는 것 할 줄 알아야 할듯
for key, value in sorted(present.items(), reverse=True):
    if value == 1:
        print(key)

"""