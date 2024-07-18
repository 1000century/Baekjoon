N = int(input())
count = 0

div = 5
step = 1
while True:
    if N //div == 0:
        break
    else:
        count = count + (N//div) * step
        div = div*5
print(count)
