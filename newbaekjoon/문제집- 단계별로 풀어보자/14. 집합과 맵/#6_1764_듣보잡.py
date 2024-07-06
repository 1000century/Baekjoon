import sys
N,M = map(int,sys.stdin.readline().split())
dict = {}
for _ in range(2*N):
    p = sys.stdin.readline().strip()
    if dict.get(p) == None:
        dict[p] = 1
    else:
        dict[p] = dict[p] + 1
count = 0
G = []
for _ in dict:
    if dict.get(_) == 2:
        count = count +1
        G.append(_)
print(len(G))
G_1 = sorted(G)

for _ in G_1:
    print(_)
