N = int(input())

a = []
for _ in range(10000):
    a.append(0)
for _ in range(N):
    A, B = map(int,input().split())
    X = 100*A+B
    print(X)
    for i in range(10):             # 색종이 한변길ㅇ이 10
        for j in range(10):         # 색종이 한변길이 10
            a[X+100*i+j] = 1
    print(a.count(1))
print(a.count(1))


