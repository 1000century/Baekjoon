# (세현)

R, C = map(int,input().split())
alpha = [list(input()) for _ in range(R)]
answer = 0

q = set()
q.add((0,0,1,alpha[0][0]))
while q:
	pr,pc,cnt,new = q.pop()
	answer = max(answer,cnt)
	for nr,nc in [(pr+1,pc),(pr-1,pc),(pr,pc+1),(pr,pc-1)]:
		if not (0<=nr<R and 0<=nc<C):
			continue
		if alpha[nr][nc] in new:
			continue
		q.add((nr,nc,cnt+1,new+alpha[nr][nc]))
print(answer)