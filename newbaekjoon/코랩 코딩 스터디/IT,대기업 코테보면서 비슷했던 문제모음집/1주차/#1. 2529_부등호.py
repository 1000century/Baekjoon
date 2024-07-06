import sys
input = sys.stdin.readline

k = int(input())
X = list(input().split())

biggest = 10**(k+1) -1
smallest = 10**(k-1)
print(biggest,smallest)
i = smallest
while i <=biggest:
	t = str(i)
	if len(t) == k:
		t = "0" + t
	
	num = {t[0]}	
	for j in range(k):
		if t[j+1] in num:
			i = (int(t[:j+2])+1)*(10**(k-j-1))
			isit = 0
			break
		num.add(t[j+1])

		if (t[j] < t[j+1] and X[j] == "<") or (t[j] > t[j+1] and X[j] == ">"):
			isit = 1
		else:
			i = (int(t[:j+1])+1)*(10**(k-j))
			isit = 0
			break
	if isit == 1:
		m = t
		tempM = i
		break



i = biggest
while i >= smallest:
	t = str(i)
	if len(t) == k:
		t = "0" + t
	if len(set(t)) != k+1:
		i = i-1
		continue
	isit = 0

	for j in range(k):
		if (t[j] < t[j+1] and X[j] == "<") or (t[j] > t[j+1] and X[j] == ">"):
			isit = 1
		else:
			i = (int(t[:j+2])-1)*(10**(k-j-1))
			isit = 0
			break
	if isit == 1:
		M = t
		break

print("쩡답")
print(M)
print(m)


