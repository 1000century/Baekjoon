import sys

A = [0]
for _ in range(9):
    p = sys.stdin.readline().strip().split()
    X = list(map(int,p))

    if max(X) >= max(A):
        result = [max(X),_+1,X.index(max(X))+1]
        A.append(max(X))
print(result[0])
print(result[1],result[2], sep= " ")

"""만약에 모든 수가 0 이러마녀
max(X) > max(A) 이런식으로 가면 안됨
>= 으로 해줘야함
"""