# 풀이 1 bfs


# (세현)

R,C = map(int,input().split())
X = [list(input()) for _ in range(R)]

stack= set()
stack.add((0,0,1,X[0][0]))

ans = 0
while stack:
	r,c,cnt,alpha = stack.pop()
	ans = max(ans,cnt)

	for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
		if nr<0 or nr>=R or nc<0 or nc>=C:
			continue
		if X[nr][nc] not in alpha:
			stack.add((nr,nc,cnt+1,alpha+X[nr][nc]))
print(ans)