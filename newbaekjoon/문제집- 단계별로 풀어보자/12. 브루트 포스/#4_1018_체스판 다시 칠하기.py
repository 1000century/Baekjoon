nbd = input()
N,M = map(int,nbd.split())
A = []
X = [1, -1]
Y = [-1,1]
for _ in range(N):
    new_string = input().strip()
    new_string = new_string.replace("W","1 ")
    new_string = new_string.replace("B","0 ")
    new_string = new_string.split()
    B=[]
    for i in new_string:
        B.append(int(i))
    A.append(B)
B = []
for i in range(N-7) :           # N은 높이
    for j in range(M-7):        # M은 가로줄
        count = 0
        for s in range(4):
            for t in range(4):              # t는 몇 번째 문자
                if A[i+2*s][j+2*t] == 1:                # A[0246][0246]
                    count= count + 1
                if A[i+2*s][j+2*t+1] == 0:            # A[0246][1357]
                    count= count + 1
                if A[i+2*s+1][j+2*t] == 0:
                    count= count + 1
                if A[i+2*s+1][j+2*t+1] == 1:
                    count= count + 1
        result = min(count,64-count)
        B.append(result)
print(min(B))