# (세현)
N = int(input())
X = []
for _ in range(N):
	X.append(list(map(int,input().split())))

for i in range(1,N):
	before = X[i-1]
	now = X[i]
	
	Ri = min(now[0] + before[1],now[0] + before[2])
	Gi = min(now[1] + before[0],now[1] + before[2])
	Bi = min(now[2] + before[0],now[2] + before[1])
	X[i] = [Ri,Gi,Bi]

print(min(X[-1]))