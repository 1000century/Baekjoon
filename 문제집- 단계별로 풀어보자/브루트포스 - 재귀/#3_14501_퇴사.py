# 못 풀었음..

import sys
N = int(sys.stdin.readline().strip())
T = []
P = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().strip().split())
    T.append(a)
    P.append(b)
print(T,P)

def tmr(N,working_day):
    if working_day[-1] == 0:
        if len(working_day) == N:
            return working_day
        else: ## 만약 일할 수 있는 날이 남으면
            return working_day

    elif working_day[-1] == 1:
        t = T[len(working_day)-1]
        if len(working_day) + (t-1) < N:
            for _ in range(t-1):
                working_day.append(0)
            return working_day
        else:
            for _ in range(N-len(working_day)):
                working_day.append(0)
            return working_day

def next_day(working_day,N,Y):
    working_day.append(Y)
    tt = T[1]
    tmr(N,working_day)
    return working_day

possiblities = 2**N

def benefit(ist):
    sum = 0
    for i in range(len(ist)):
        if ist[i] == 1:
           sum = sum + P[i]
    return sum



my_list = []
while len(my_list) <= N:
    ans = 0
    for p in range(possiblities):
        while p != 0:

            y = p % 2
            p = p // 2
            next_day(my_list,N,y)
        if benefit(my_list) >= ans:
            ans = benefit(my_list)

print(ans)
