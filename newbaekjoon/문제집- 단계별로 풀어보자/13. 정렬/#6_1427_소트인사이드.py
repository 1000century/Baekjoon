N = list(input())
N = sorted(N)
a = ''
for _ in range(len(N)):
    a= a +N[len(N)-_-1]
print(int(a))
