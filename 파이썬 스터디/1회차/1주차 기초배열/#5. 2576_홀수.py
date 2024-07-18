sum = 0
holsu = 999
for _ in range(7):
    a = int(input())
    if a % 2 != 0:
        holsu = min(holsu,a)
        sum = sum + a
    
if holsu == 999:
    print(-1)
else:
    print(sum)
    print(holsu)