# (세현)

H,W = map(int,input().split())
X = list(map(int,input().split()))
count = 0
for h in range(H):
	rtend = "not determined"
	for w in range(W):
		if X[w] > h:
			if rtend!="not determined":
				count = count + w-rtend-1
			rtend = w
print(count)