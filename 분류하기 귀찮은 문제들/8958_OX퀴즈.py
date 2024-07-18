N = int(input())
for _ in range(N):
    M = input()
    count = 0
    M = M.split("X")
    M = [_ for _ in M if _ != '']
    for i in M:
        x = len(i)
        count = count + x*(x+1)/2
    print(int(count))

