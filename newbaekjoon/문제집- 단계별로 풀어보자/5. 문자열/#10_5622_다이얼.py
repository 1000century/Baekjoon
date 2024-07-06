a = list(input())
a = [int(ord(x))-65 for x in a]
b = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
c = 0
for _ in range(len(a)):
    c = c+b[a[_]]
print(c)