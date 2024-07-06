from collections import deque

M,N = map(int,input().split())

A = [list(map(int,input().replace(""," ").split())) for _ in range(M)]

visited = set()
Q = deque([])
for i in range(N):
	if (0,i) not in visited:
		visited.add((0,i))
		if A[0][i] == 0:
			Q.append([0,i])
	while Q:
		p,q = Q.popleft()
		for x,y in [(p+1,q),(p-1,q),(p,q+1),(p,q-1)]:
			if 0<=x<M and 0<=y<N and (x,y) not in visited:
				visited.add((x,y))
				if A[x][y] == 0:
					if x == M-1:
						print("YES")
						exit()
					Q.append([x,y])
print("NO")