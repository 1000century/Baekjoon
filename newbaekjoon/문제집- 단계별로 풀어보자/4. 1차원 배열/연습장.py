a = []
for _ in range(10):
    element = int(input()) % 42
    a.append(element)
sorted(a)

b = []
for _ in range(10):
    if a[_] not in b:
        b.append(a[_])
print(len(b))