M= input().split()
K = list(M[0])
N = K[::-1]
B = int(M[1])
result = 0
for _ in range(len(N)):
    if ord(N[_])<60:
        result = result + int(N[_])*(B**_)
        # print(result)
    else:
        result = result + (ord(N[_])-55)*(B**_)
        # print(result)


print(result)

