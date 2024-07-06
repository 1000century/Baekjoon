N = int(input())
X =[]
for _ in range(N):
	X.append(input())
X = list(set(X))
X.sort(key=lambda x:(len(x),x))
#X.sort(key=len) >>> 이렇게만 하면  같은 key에 대해서는 원래대로 따짐
for i in X:
	print(i)