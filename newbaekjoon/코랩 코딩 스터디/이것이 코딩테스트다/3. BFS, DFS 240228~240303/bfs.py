import copy

n,m,st=map(int,input().split())
dfs_list=[[] for _ in range(n+1)]

# 간선 연결
for _ in range(m):
    a,b=map(int,input().split())
    dfs_list[a].append(b)
    dfs_list[b].append(a)

for i in range(len(dfs_list)):
    dfs_list[i] = list(set(dfs_list[i]))

bfs_list = copy.deepcopy(dfs_list)

#### DFS
d = st
dfs_list[0].append(d)
for k in range(1, n+1):
	if d in dfs_list[k]:
		dfs_list[k].remove(d)
back = [d]

while len(dfs_list[d]) != 0:
    d = min(dfs_list[d])
    back.append(d)
    dfs_list[0].append(d)
    for k in range(1, n+1):
        if d in dfs_list[k]:
            dfs_list[k].remove(d)
    while len(dfs_list[d]) ==0 and len(back) != 0:
        d = back[-1]
        back.pop()
    while len(dfs_list[d]) ==0 and len(back) == 0:
        for y in range(1,n+1):
            if len(dfs_list[y]) != 0:
                d = y
                break
        break

print(' '.join(map(str,dfs_list[0])))

#### BFS
b = st
bfs_list[0].append(b)
for q in range(1, n+1):
    if b in bfs_list[q]:
        bfs_list[q].remove(b)
while len(bfs_list[b]) != 0:
    p = min(bfs_list[b])
    bfs_list[0].append(p)
    for q in range(1,n+1):
            if p in bfs_list[q]:
                bfs_list[q].remove(p)
    if len(bfs_list[b]) == 0:
        for x in range(1,n+1):
            if len(bfs_list[x]) != 0:
                b = x
            

print(' '.join(map(str,bfs_list[0])))
