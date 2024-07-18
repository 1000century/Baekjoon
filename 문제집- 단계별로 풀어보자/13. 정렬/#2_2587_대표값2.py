b = []
for _ in range(5):
    b.append(int(input()))
b= sorted(b)
print((b[0]+b[1]+b[2]+b[3]+b[4])//5)
print(b[2])