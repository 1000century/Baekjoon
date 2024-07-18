N, K = map(int,input().split())
a = int(N**(0.5))
group = []
for _ in range(1,a+1):
    if N % _ == 0:
        group.append(_)
        group.append(N//_)
group = list(set(group))
group.sort()
if len(group)<K:
    print(0)
else:
    print(group[K-1])