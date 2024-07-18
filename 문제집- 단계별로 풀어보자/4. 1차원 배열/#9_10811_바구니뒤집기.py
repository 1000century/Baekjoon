N, M = map(int,input().split())
a = []
for _ in range(N):
    a.append(_+1)
    # 1번자리에 1번바구니 2번자리에 2번 바구니
b = a[:]

for x in range(M):
    i, j = map(int,input().split())
    k = j-i
    for g in range(k+1):
        prev = a[i+g-1]
        b[j-g-1] = prev
    a = b[:]    
for _ in range(len(b)):
    print(b[_], end=" ")
