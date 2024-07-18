N,B= map(int,input().split())
A = []
while N // B != 0:
    A.append(X%B)
    N = N//B
else:
    A.append(N%B)
print(A) ####################
B = A[::-1]
for _ in B:
    if _ > 9:
        print(chr(_+55),end="")
    else:
        print(_,end="")
