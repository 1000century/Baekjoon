N, k = map(int,input().split())
S = list(map(int,input().split()))
S = sorted(S)
S = S[::-1]
print(S[k-1])