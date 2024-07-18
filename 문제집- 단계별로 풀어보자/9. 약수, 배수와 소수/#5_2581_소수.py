M = int(input())
N = int(input())
ss = []
for i in range(M,N+1):
    A = []
    a = int(i**0.5)
    for e in range(1,a+1):
        if i % e ==0:
            A.append(e)
    if len(A) == 1:
        ss.append(i)
if 1 in ss:
    ss.remove(1)
if len(ss) == 0:
    print(-1)
else:
    sum = 0
    for _ in ss:
        sum = sum + _
    print(sum)
    print(ss[0])