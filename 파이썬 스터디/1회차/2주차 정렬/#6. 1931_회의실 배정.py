N = int(input())

confs = []
for _ in range(N):
	a,b = map(int,input().split())
	confs.append([a,b])
confs.sort(key=lambda x:(x[1],x[0]))

end = 0
ans = 0

for conf in confs:
	nextst = conf[0]
	nexten = conf[1]
	if end <=nextst:
		ans = ans + 1
		end = nexten

print(ans)
