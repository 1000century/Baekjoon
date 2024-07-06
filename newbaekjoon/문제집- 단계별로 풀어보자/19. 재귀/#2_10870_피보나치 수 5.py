n = int(input())
a1 = 0
a2 = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n-1):
        a3 = a1 + a2
        ans = a3
        a1 = a2
        a2 = a3
    print(ans)
