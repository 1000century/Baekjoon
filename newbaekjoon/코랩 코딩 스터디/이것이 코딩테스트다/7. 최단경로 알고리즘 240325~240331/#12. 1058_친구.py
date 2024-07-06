# (세현)

N = int(input())

graph = [list(input()) for _ in range(N)]

ans = []
for a in range(N):
    count = 0
    for b in range(N):
        if b == a:
            continue
        if graph[a][b] == "Y":
            count += 1
            continue
        for k in range(N):
            if graph[b][k] == "Y" and graph[k][a] == "Y":
                count += 1
                break
    ans.append(count)

print(max(ans))