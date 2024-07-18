
h = 25
t = 5

B = [h,t]
B.sort()
print(B,B[1] % B[0] )

if B[1] % B[0] == 0:
    if h >= t:
        print(h//t, 1)
    else:
        print(1,t//h)
else:
    while True:
        sum = B[0]+B[1]
        m = sum - min(B)
        M = sum - max(B)
        if m === 0:
            print(h // M, t//M)
            break
        else:
            B_1 = B
            B[1] = B_1[0]
            B[0] = B_1[1] % B_1[0]
            print("ddd", B_1, B)

