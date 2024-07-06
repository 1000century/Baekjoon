N = int(input())
A = []
result = 0
for _ in range(N):
    cmd = input()
    if cmd == "ENTER":
        A = list(set(A))
        count = len(A)
        result = result + count
        A = []               # 준비작업 - 초기화
    else:
        A.append(cmd)
A = list(set(A))
count = len(A)
result = result + count
print(A,result)
