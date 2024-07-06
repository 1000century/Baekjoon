# 10773 제로
K = int(input())
Stack = []
for _ in range(K):
    X = int(input())
    if X != 0:
        Stack.append(X)
    else:
        Stack.pop()
sum = 0
for element in Stack:
    sum = sum + element
print(sum)