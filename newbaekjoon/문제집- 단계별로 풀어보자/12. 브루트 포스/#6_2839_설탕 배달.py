N = int(input())
a =  N //5
for i in range(a+1):
    if (N - 5*(a-i)) % 3 == 0:
        print(a-i+(N - 5*(a-i)) // 3)
        exit()
print(-1)
