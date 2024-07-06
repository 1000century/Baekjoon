H,M = map(int,input().split(" "))
wannawakeup = H*60+M
if wannawakeup - 45 < 0:
    shouldwakeup = wannawakeup - 45 + 1440
else:
    shouldwakeup = wannawakeup -45

print(shouldwakeup//60,shouldwakeup%60)
