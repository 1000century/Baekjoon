X = int(input())
N = int(input())
ans = 0
for i in range (1,N+1):
    a,b = map(int, input().split(" "))
    c = a*b
    ans += c


print("Yes") if ans == X else print("No")