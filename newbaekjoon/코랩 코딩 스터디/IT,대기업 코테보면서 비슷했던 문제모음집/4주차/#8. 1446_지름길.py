N, D = map(int,input().split())

dist = [i for i in range(0,D+1)]
graph = []
for _ in range(N):
	st,en,d = map(int,input().split())
	graph.append((st,en,d))
graph.sort(key=lambda x:x[1])
for st, en, d in graph:
	for i in range(en, D+1):
		dist[i] = min(dist[i],min(dist[en],dist[st] + d)+(i-en))
print(dist[-1])
