# (세현)

N = int(input())
M = int(input())
light = list(map(int,input().split()))

dist = []

if light[0] != 0:
	dist.append(light[0]*2)
for i in range(M-1):
	dist.append(light[i+1]-light[i])
if light[-1] != N:
	dist.append((N-light[-1])*2)

if max(dist)%2 != 0:
	print(max(dist)//2+1)
else:
	print(max(dist)//2)