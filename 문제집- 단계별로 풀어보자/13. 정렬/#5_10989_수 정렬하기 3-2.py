N = int(input())
Y = []
for _ in range(N):
    Y.append(int(input()))
Y = list(map(int,input().split()))
result1 = sorted(list(set(Y)))
dict = {}
for _ in range(len(result1)):
    dict[result1[_]] = _
for _ in Y:
    print(dict[_])

