def test():
    n = int(input())

    dp = [0] * (n+1)

    if n ==1:
        print(1)
        return
    if n ==2:
        print(2)
        return
    if n ==3:
        print(4)
        return
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])


T = int(input())
for _ in range(T):
    test()
