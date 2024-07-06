# i번째 집은 i-1, i+1과 다르면 됨..
# i-1,i,i+1 이 다 다르다는 말이 아님.

N = int(input())

dp_r,dp_g,dp_b = [0],[0],[0]
r,g,b = 0,0,0

for i in range(1,N+1):
	r,g,b = map(int,input().split())
	dp_r.append(r+min(dp_b[i-1], dp_g[i-1]))
	dp_g.append(g+min(dp_r[i-1], dp_b[i-1]))
	dp_b.append(b+min(dp_r[i-1], dp_g[i-1]))

print(min(dp_r[-1],dp_g[-1],dp_b[-1]))