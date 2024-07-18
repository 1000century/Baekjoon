#5_12789_도키도키 간식드리미
N = int(input())
group = list(map(int,input().split()))
storage = [0]
target = 1
ans = 0
for i in range(N):
    while storage[-1] == target:
        storage.pop()
        target = target + 1
    if group[i] == target:
        target = target + 1
    else:
        if group[i] <group[i+1]:
            ans = "Sad"
            break
        elif group[i] > group[i+1] and group[i+1] == target:
            group[i+1] = group[i]
            target = target + 1
        elif group[i] > group[i+1] and group[i+1] != target:
            storage.append(group[i])
while storage[-1] == target:
    storage.pop()
    target = target + 1

if ans == "Sad":
    print("Sad")
else:
    if target == N+1:
        print("Nice")
    else:
        print(target)
        print("Sad")

