
"""
3/7 11:03~11:46
"""
key = input()
N = len(key)
X = []
for i in range(N):
    X.append([i,key[i]])
X_sorted =sorted(X,key=lambda x: x[1])
order = []
for i in range(len(X_sorted)):
    order.append(X_sorted[i][0])


mystery_sentence = input()
vertical = len(mystery_sentence) // N
mystery = [[] for _ in range(vertical)]
for j in range(vertical):
    for i in range(N):
        mystery[j].append(mystery_sentence[i*vertical + j])
for i in range(vertical):
    for j in range(N):
        print(mystery[i][order.index(j)],end="")

