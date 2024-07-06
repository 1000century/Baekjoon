import sys

p = []
for _ in range(5):
    q = sys.stdin.readline().strip()
    p.append(q+"!!!!!!!!!!!!!!!")
    print(p)
alpha = []
for _ in range(15):   ## 나머지가 _인수들을 모을거야
    q = []
    for x in range(5):
        q.append(list(p[x])[_])
    for y in range(5):
        alpha.append(q[y])
for _ in range(75):
    if alpha[_] != "!":
        print(alpha[_],end="")

    