a = input().split()[1]
a = int(a)
l = list(map(int,input().split()))

k = []
for x in l:
    if x < a:
        k.append(x)
for element in k:
    print(element, end=" ")