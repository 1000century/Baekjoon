# (세현)
"""
https://www.acmicpc.net/problem/2668

"""
N = int(input())
arr = []
result = set()
for i in range(1,N+1):
	x = int(input())
	arr.append(x)


for st in range(1,N+1):
#	print("_________________________",st)
	if st in result:
		continue
	n = arr[st-1]
	visited = set()
	while True:
		visited.add(n)
		if n == st:
			for t in visited:
				result.add(t)
			break
		if n in result:
			break
		if arr[n-1] in visited:
			break
		n = arr[n-1]

ans = []
for i in result:
	ans.append(i)
ans.sort()
print(len(ans))
print(*ans,sep='\n')

