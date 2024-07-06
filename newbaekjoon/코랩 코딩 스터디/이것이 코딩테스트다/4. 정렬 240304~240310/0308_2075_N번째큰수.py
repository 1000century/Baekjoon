
"""
3/7 11:50~11:57
"""
X = []
N = int(input())
for _ in range(N):
    X.extend(list(map(int,input().split())))
    X.sort(reverse = True)
    X = X[:N]
print(X[-1])