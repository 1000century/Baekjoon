import sys
N,M = map(int,input().split())  # 한줄에 M개씩 N개 열
A = [

]
B= [

]
for _ in range(N):
    X = sys.stdin.readline().strip()
    Y = list(map(int,X.split()))
    A.append(Y)


for _ in range(N):
    X = sys.stdin.readline().strip()
    Y = list(map(int,X.split()))
    B.append(Y)


for _ in range (N):
    for q in range(M):
        print(A[_][q]+B[_][q],end=" ")
    print()    
    