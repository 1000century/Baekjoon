N = int(input())
a = 0
for _ in range(N):
    S = input()
    len_s = len(S)

    ssss = list(set(S))

    T = [S[0]]
    for i in range(1,len_s ):
        if S[i] != S[i-1]:
            T.append(S[i])
        else:
            continue
    if len(T) == len(ssss):
        a+=1
print(a)

