"""
24.03.10
"""

N = int(input())
X = []

for _ in range(N):
    X.append(int(input()))
    X = list(set(X))
X.sort()

least = 4


for i in range(len(X)):
	start = X[i]
	count = 0
	isit  = []
	for k in range(0,5):
		isit.append(start+k)
	for j in range(i,len(X)):
		if X[j] in isit:
			count = count +1
	least = min(5-count,least)

print(least)