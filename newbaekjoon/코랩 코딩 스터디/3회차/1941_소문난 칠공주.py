# (세현)

import sys
sys.setrecursionlimit(10000)
ans = set()

def princess(p,visited,sc,yc):
	if sc+yc == 7:
		x = tuple(sorted(list(visited)))
		if x not in ans:
			ans.add(x)
	else:
		for ij in visited:
			ii,jj = ij//10, ij%10
			for nx,ny in [(ii+1,jj),(ii-1,jj),(ii,jj+1),(ii,jj-1)]:
				if not (0<=nx<5 and 0<=ny<5):
					continue
				q = 10*nx+ny
				if q in visited:
					continue
				if yc+(p[nx][ny]=="Y")==4:
					continue
				visited.add(q)
				princess(p,nx,ny,visited,sc+(p[nx][ny]=="S"),yc+(p[nx][ny]=="Y"))
				visited.remove(q)
	

p = [list(input()) for _ in range(5)]
for i in range(5):
	for j in range(5):
		k = 10*i+j
		s = (p[i][j]=="S")
		y = (p[i][j] == "Y")
		princess(p,{k},s,y)
print(len(ans))
