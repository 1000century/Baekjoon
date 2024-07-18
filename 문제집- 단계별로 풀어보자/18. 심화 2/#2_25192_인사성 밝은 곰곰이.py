### 시간초과

N = int(input())
A = []
result = 0
count = 0
for _ in range(N):
    cmd = input()
    if cmd == "ENTER":
        A = []
        result = result + count
        count = 0               # 준비작업 - 초기화
    else:
        if cmd not in A:
            A.append(cmd)
            count = count + 1
        else:
            A.remove(cmd)
            count = count
result = result + count
print(result)
